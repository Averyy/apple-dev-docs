# Adding parameters to plug-ins

**Framework**: Professional-Video-Applications  
**Role**: Article

Create standard and custom user-facing parameters for your plug-in that will appear in the inspector.

#### Overview

Once a plug-in is invoked by a host application, the host application asks for the plug-in’s parameter list by calling the [`addParameters()`](../professional_video_applications/fxtileableeffect/addparameters%28%29.md) method. This method is declared in the `FxBaseEffect` protocol, which is inherited by the [`FxTileableEffect`](../professional_video_applications/fxtileableeffect.md) protocol. The host application then displays the parameters in its inspector.

##### Add a parameter

The FxPlug SDK includes methods for adding these standard types of parameters:

- Floating-point, integer, and percent sliders
- Angle slider
- Toggle button (checkbox)
- RGB or RGBA color
- Point
- Popup menu
- String
- Histogram
- Gradient
- Path picker
- Font menu
- Help button
- Push button
- Image Reference
- Group

![Examples of standard parameters](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3668805@2x.png)

In the [`addParameters()`](../professional_video_applications/fxtileableeffect/addparameters%28%29.md) method, a plug-in first calls the [`api(for:)`](../professional_video_applications/proapiaccessing/api%28for%29.md) method (defined by the `PluginManager` framework) to get the host API object that implements the protocol. It then adds parameters, one by one, using methods in the [`FxParameterCreationAPI_v5`](../professional_video_applications/fxparametercreationapi_v5.md) protocol.

For example, the following code shows an `-addParametersWithError:` method from a simple opacity filter:

> ❗ **Important**: Parameter IDs must be in the range of `[1, 9998]`. IDs outside of this range are invalid.

**Swift**:

```swift
func addParameters() throws {
    let paramAPI = _apiManager!.api(for: FxParameterCreationAPI_v5.self) as! FxParameterCreationAPI_v5
        
    paramAPI.addFloatSlider(withName: "Opacity", parameterID: 1, defaultValue: 1.0, parameterMin: 0.0, parameterMax: 100.0, sliderMin: 0.0, sliderMax: 10.0, delta: 0.1, parameterFlags: FxParameterFlags(kFxParameterFlag_DEFAULT))
}
```

**Objective-C**:

```objc
enum 
{ 
    kOpacityID = 1
}; 

- (BOOL)addParametersWithError:(NSError**)error
{
    id<FxParameterCreationAPI_v5> paramAPI = [apiManager apiForProtocol:@protocol(FxParameterCreationAPI_v5)];

    BOOL success =[paramAPI addFloatSliderWithName:@"Opacity"
                                       parameterId:kOpacityID
                                      defaultValue:1.0
                                      parameterMin:0.0
                                      parameterMax:100.0
                                         sliderMin:0.0
                                         sliderMax:10.0
                                             delta:0.1 
                                    parameterFlags:kFxParameterFlag_DEFAULT];
    return success;
} 
```

> **Note**:  A Mix slider parameter is automatically added filter plug-ins, and a Publish OSC toggle parameter is automatically added in Motion to any plug-in that contains onscreen controls. The Publish OSC toggle parameter is never visible in Final Cut Pro.

##### Create a custom parameter

In addition to the standard parameter types, you can use the following method to create a custom parameter with an opaque data type:

**Swift**:

```swift
addCustomParameter(withName:parameterID:defaultValue:parameterFlags:)
```

**Objective-C**:

```objc
-addCustomParameterWithName:parameterID:defaultValue:parameterFlags
```

Each custom parameter must be associated with a custom parameter view, which is defined by the methods in [`FxCustomParameterViewHost_v2`](../professional_video_applications/fxcustomparameterviewhost_v2.md).

##### Interact with parameters

When a user changes a parameter control for an FxPlug plug-in, the host application calls the [`parameterChanged(_:at:)`](../professional_video_applications/fxtileableeffect/parameterchanged%28_,at%29.md) plug-in method. This is useful for a plug-in that changes the state of other parameters. For example, if the user changes a toggle button, the plug-in can hide or reveal other parameters during [`parameterChanged(_:at:)`](../professional_video_applications/fxtileableeffect/parameterchanged%28_,at%29.md).

##### Handle user interaction for custom UI parameters

Custom UI parameters let developers draw directly to a custom UI and create their own controls in a space that the host application makes for them in the inspector. The host application handles user interaction for custom parameters in a different way than standard UI parameters. For example, when you develop custom parameters, they must conform to the [`FxCustomParameterViewHost_v2`](../professional_video_applications/fxcustomparameterviewhost_v2.md) protocol. An example of this can be found in the `FxSimpleColorCorrector` sample plug-in.

In your plug-in, custom parameters conform to the `FxParameterViewHost` protocol by implementing a [`createView(forParameterID:)`](../professional_video_applications/fxcustomparameterviewhost_v2/createview%28forparameterid%29.md) method that provides an [`NSView`](../AppKit/nsview.md) subclass to the host app. Like any other `NSView` subclass, this custom view draws itself in a window and receives notification of any user actions such as mouse, key, and tablet events. In response to user events, the custom view sets parameter values. Usually it sets the value of a custom parameter. The host application notices that a parameter value has changed and calls the plug-in to render with the new parameter values.

The plug-in can create a custom view object programmatically or retrieve it from a `XIB` file (created in Xcode’s Interface Builder and placed in your plug-in’s `Resources` folder).

Your plug-in’s custom view methods must call the [`FxCustomParameterActionAPI_v4`](../professional_video_applications/fxcustomparameteractionapi_v4.md) host API [`startAction(_:)`](../professional_video_applications/fxcustomparameteractionapi_v4/startaction%28_%29.md) method before your plug-in accesses any parameter values, and then call the [`endAction(_:)`](../professional_video_applications/fxcustomparameteractionapi_v4/endaction%28_%29.md) method after it has finished accessing the parameter values. This lets the host application set up and restore the internal state.

##### Update versioning for your plug-in’s parameters

As you develop plug-ins over time, you may need to deprecate, add, or update your parameters, like changing a default value or range.

To ensure that projects using your older plug-ins still function correctly, use [`FxVersioningAPI`](../professional_video_applications/fxversioningapi.md) to find out the version of the plug-in that’s used with a project. With this information, you can branch your parameter code, update your project, and handle special cases as needed.

For example, if you create a version 1 brightness filter with a floating point slider and apply it to a project, the project saves the plug-in’s version number along with the slider value. On subsequent launches of the project, you can query [`versionAtCreation()`](../professional_video_applications/fxversioningapi/versionatcreation%28%29.md) and check for a version number of `1`.

See [Versioning and obsoleting old plug-ins](./versioning-and-obsoleting-old-plug-ins.md) for more information.

> 💡 **Tip**: If you later update the brightness filter to use a second parameter, update the version of your plug-in. Then, on subsequent launches, do a version check and add a second path for a version number of `2`.

## Topics

### Parameter APIs
- [protocol FxParameterCreationAPI_v5](../professional_video_applications/fxparametercreationapi_v5.md)
  Defines the methods provided by the host application to create parameters.
- [protocol FxParameterRetrievalAPI_v6](../professional_video_applications/fxparameterretrievalapi_v6.md)
  Defines the functions the application provides to retrieve parameter values.
- [protocol FxParameterRetrievalAPI_v7](../professional_video_applications/fxparameterretrievalapi_v7.md)
  Adds a method to retrieve the image information about an image parameter.
- [protocol FxParameterSettingAPI_v5](../professional_video_applications/fxparametersettingapi_v5.md)
  Defines the functions the application provides to set parameter values.
- [protocol FxParameterSettingAPI_v6](../professional_video_applications/fxparametersettingapi_v6.md)
  Defines the functions the application provides to set parameter flags.
- [protocol FxDynamicParameterAPI_v3](../professional_video_applications/fxdynamicparameterapi_v3.md)
  Allows your plugin to create parameters on-the-fly.
### Custom Parameter APIs
- [protocol FxCustomParameterViewHost_v2](../professional_video_applications/fxcustomparameterviewhost_v2.md)
  Defines the methods a plug-in needs to implement to associate a custom NSView with one of its parameters.
- [protocol FxCustomParameterActionAPI_v4](../professional_video_applications/fxcustomparameteractionapi_v4.md)
  Defines the methods the host application provides to support a custom parameter view.
- [protocol FxCustomParameterInterpolation_v2](../professional_video_applications/fxcustomparameterinterpolation_v2.md)
  Defines the methods a plug-in needs to implement to support keyframing custom parameters.
### Constants
- [typealias FxParameterFlags](../professional_video_applications/fxparameterflags.md)
  These constants specify the characteristics of parameters display.
- [typealias FxHistogramChannel](../professional_video_applications/fxhistogramchannel.md)
  Constants used to identify which channel a histogram operation should apply to.

## See Also

### User interface
- [Adding onscreen controls to plug-ins](./adding-onscreen-controls-to-plug-ins.md)
  Simplify user interaction by using onscreen controls for your FxPlug plug-in.
- [protocol FxPathAPI_v3](../professional_video_applications/fxpathapi_v3.md)
  An API that defines the methods to retrieve information about paths, shapes, and masks the user has drawn on an object.
- [protocol FxUndoAPI](../professional_video_applications/fxundoapi.md)
  An API that defines the methods that the host app implements to handle plug-in management of the host app’s undo queue.
- [protocol FxCommandAPI](../professional_video_applications/fxcommandapi.md)
  Commands that you can tell the host to perform.
- [protocol FxCommandAPI_v2](../professional_video_applications/fxcommandapi_v2.md)
  Adds functionality to move the playhead to a specific timeline time.
- [protocol FxRemoteWindowAPI](../professional_video_applications/fxremotewindowapi.md)
  A protocol that allows the plug-in to request that the host create a window.
- [protocol FxRemoteWindowAPI_v2](../professional_video_applications/fxremotewindowapi_v2.md)
  A protocol that allows the plug-in to request that the host create a window with a defined minimum and maximum size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/adding-parameters-to-plug-ins)*