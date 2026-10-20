# kCMMInitializeTransformProcName

**Framework**: ColorSync  
**Kind**: var  
**Role**: Global Variable

The CMM bundle info-dictionary key whose value is the name of the function that initializes a color transform.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
var kCMMInitializeTransformProcName: Unmanaged<CFString>!
```

```c
extern CFStringRef kCMMInitializeTransformProcName;
```

## See Also

### Registering plug-in entry points
- [var kCMMApplyTransformProcName: Unmanaged<CFString>!](./kcmmapplytransformprocname.md)
  The CMM bundle info-dictionary key whose value is the name of the function that applies a color transform.
- [var kCMMCreateTransformPropertyProcName: Unmanaged<CFString>!](./kcmmcreatetransformpropertyprocname.md)
  The CMM bundle info-dictionary key whose value is the name of the function that creates a transform property.
- [var kCMMInitializeLinkProfileProcName: Unmanaged<CFString>!](./kcmminitializelinkprofileprocname.md)
  The CMM bundle info-dictionary key whose value is the name of the function that initializes a device-link profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcmminitializetransformprocname)*