# init(plugIn:viewNibName:)

**Framework**: Quartz  
**Kind**: init  
**Role**: Initializer

Creates and initializes a controller for the specified `QCPlugIn` object and nib file.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
init!(plugIn: QCPlugIn!, viewNibName name: String!)
```

```objc
- (id) initWithPlugIn:(QCPlugIn *) plugIn viewNibName:(NSString *) name;
```

## Return Value

A `QCPlugInViewController` object.

## Parameters

- `plugIn`: A `QCPlugIn` object that uses internal settings.
- `name`: The name of the nib file that contains the view for the custom patch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginviewcontroller/init(plugin:viewnibname:))*