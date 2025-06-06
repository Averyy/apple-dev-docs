# init(plugIn:viewNibName:)

**Framework**: Quartz  
**Kind**: init

Creates and initializes a controller for the specified `QCPlugIn` object and nib file.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
init!(plugIn: QCPlugIn!, viewNibName name: String!)
```

#### Return Value

A `QCPlugInViewController` object.

## Parameters

- `plugIn`: A   object that uses internal settings.
- `name`: The name of the nib file that contains the view for the custom patch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginviewcontroller/init(plugin:viewnibname:))*