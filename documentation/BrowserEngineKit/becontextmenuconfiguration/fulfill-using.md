# fulfill(using:)

**Framework**: BrowserEngineKit  
**Kind**: method

Fulfills the configuration with a concrete configuration. Once fulfilled, the context menu presentation will begin. You should call this method as soon as you have determined that a menu presentation is possible for the configuration, as to minimize the delay between the context menu gesture’s recognition and the menu’s presentation. If no menu presentation is possible, fulfill with a `nil` configuration.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
func fulfill(using configuration: UIContextMenuConfiguration?) -> Bool
```

#### Return Value

`true` if the configuration was fulfilled in time to present the contextual menu; `false` otherwise.

#### Discussion

There is a system-defined timeout before the configuration is cancelled, where no menu presents. This method returns `YES` if the configuration did successfully prepare, and `NO` otherwise.

rather than this object.

Supplies the complete contextual menu configuration.

#### Overview

The system expects your app to call `fulfill(using:)` within a certain time; if you don’t call the method before this time elapses, the system doesn’t display the contextual menu as if you called this method with `nil` as the parameter.

Once you fulfill the configuration, your [`UIContextMenuInteractionDelegate`](https://developer.apple.com/documentation/UIKit/UIContextMenuInteractionDelegate) refers the `configuration` object you supply to configure the contextual menu, and not the instance of `BEContextMenuConfiguration` that you passed to [`contextMenuInteraction(_:configurationForMenuAtLocation:)`](https://developer.apple.com/documentation/UIKit/UIContextMenuInteractionDelegate/contextMenuInteraction(_:configurationForMenuAtLocation:)).

## Parameters

- `configuration`: The calculated configuration for the contextual menu. To avoid presenting the contextual menu, pass  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/becontextmenuconfiguration/fulfill(using:))*