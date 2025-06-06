# Integrating CarPlay with Your Navigation App

**Framework**: CarPlay

Configure your navigation app to work with CarPlay by displaying your custom map and directions.

**Availability**:
- iOS 15.4+
- Xcode 15.0+

#### Overview

Coastal Roads is a sample navigation app that demonstrates how to display a custom map and navigation instructions in a CarPlay–enabled vehicle. Coastal Roads integrates with the CarPlay framework by implementing the map and additional `CPTemplate` subclasses, such as [`CPGridTemplate`](CPGridTemplate.md) and [`CPListTemplate`](CPListTemplate.md). This sample’s iOS app component provides a logging interface to help you understand the life cycle of a CarPlay app.

##### Handle Communication with Carplay

After the app connects to CarPlay, it immediately sets a root template to display content onscreen. The sample sets the root template on the `CPInterfaceController` when the app connects to CarPlay. In all navigation apps, the root template must be an instance of `CPMapTemplate` and contain no additional graphics or UI elements.

The following code shows an example implementation of setting a root template:

```swift
// MARK: CPTemplateApplicationSceneDelegate

func interfaceController(_ interfaceController: CPInterfaceController, didConnectWith window: CPWindow, style: UIUserInterfaceStyle) {
    MemoryLogger.shared.appendEvent("Connected to CarPlay window.")

    carplayInterfaceController = interfaceController
    carplayInterfaceController!.delegate = self
    
    window.rootViewController = mainMapViewController
    carWindow = window
    
    let mapTemplate = CPMapTemplate.coastalRoadsMapTemplate(compatibleWith: mainMapViewController.traitCollection, zoomInAction: {
        MemoryLogger.shared.appendEvent("Map zoom in.")
        self.mainMapViewController.zoomIn()
    }, zoomOutAction: {
        MemoryLogger.shared.appendEvent("Map zoom out.")
        self.mainMapViewController.zoomOut()
    })

    mapTemplate.mapDelegate = self

    baseMapTemplate = mapTemplate

    installBarButtons()

    interfaceController.setRootTemplate(mapTemplate, animated: true) { (success, _) in
        if success {
            MemoryLogger.shared.appendEvent("Root MapTemplate set successfully")
        }
    }
}
```

##### Render a Map As the Base Template

Coastal Roads demonstrates various templates in CarPlay. The sample includes an image to serve as the map. All overlays must be a type of template that CarPlay provides. The map must cover the entire screen, which the sample accomplishes using constraints. The `CPMapTemplate` also provides native support for zooming and panning. Additional functionality, such as customizing default button behavior, is available.

The following code shows an example implementation of customizing the default behavior of the panning, preview, and trip start actions on `CPMapTemplate`:

```swift
extension TemplateManager: CPMapTemplateDelegate {

    func mapTemplate(_ mapTemplate: CPMapTemplate, panWith direction: CPMapTemplate.PanDirection) {
        mainMapViewController.panInDirection(direction)
    }

    func mapTemplate(_ mapTemplate: CPMapTemplate, selectedPreviewFor trip: CPTrip, using routeChoice: CPRouteChoice) {
        mainMapViewController.setPolylineVisible(true)
    }

    func mapTemplate(_ mapTemplate: CPMapTemplate, startedTrip trip: CPTrip, using routeChoice: CPRouteChoice) {

        MemoryLogger.shared.appendEvent("Beginning navigation guidance.")

        let navSession = mapTemplate.simulateCoastalRoadsNavigation(
            trip: trip,
            routeChoice: routeChoice,
            traitCollection: mainMapViewController.traitCollection)
        navigationSession = navSession

        simulateNavigation(for: navSession, maneuvers: mapTemplate.coastalRoadsManeuvers(compatibleWith: mainMapViewController.traitCollection))
    }
```

See [`CPMapTemplateDelegate`](CPMapTemplateDelegate.md) for more information.

## See Also

- [class CPTemplateApplicationDashboardScene](cptemplateapplicationdashboardscene.md)
  A CarPlay scene that controls your app’s dashboard navigation window.
- [protocol CPTemplateApplicationDashboardSceneDelegate](cptemplateapplicationdashboardscenedelegate.md)
  The methods for responding to the life-cycle events of your navigation app’s dashboard scene.
- [class CPMapTemplate](cpmaptemplate.md)
  A template that displays a navigation overlay that your app draws on the map.
- [class CPSearchTemplate](cpsearchtemplate.md)
  A template that provides the ability to search for a destination and see a list of search results.
- [class CPVoiceControlTemplate](cpvoicecontroltemplate.md)
  A template that displays a voice control indicator during audio input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/integrating-carplay-with-your-navigation-app)*