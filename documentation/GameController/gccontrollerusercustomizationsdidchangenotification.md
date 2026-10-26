# GCControllerUserCustomizationsDidChangeNotification

**Framework**: Game Controller  
**Kind**: var  
**Role**: Global Variable

A notification that posts when the user customizes the button mappings or other settings of a controller.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```c
extern NSString * const GCControllerUserCustomizationsDidChangeNotification;
```

#### Discussion

Use this notification to update your interface when the mappings change. The notification object is the [`GCController`](./gccontroller.md) object that the user customizes.

The system posts this notification on the main thread.

## See Also

### Remapping input elements
- [var hasRemappedElements: Bool](./gcphysicalinputprofile/hasremappedelements.md)
  A Boolean value that indicates whether the user remaps elements in this profile.
- [func mappedElementAlias(forPhysicalInputName: String) -> String](./gcphysicalinputprofile/mappedelementalias%28forphysicalinputname%29.md)
  Returns the name of the input element to which the user remaps the given physical element.
- [func mappedPhysicalInputNames(forElementAlias: String) -> Set<String>](./gcphysicalinputprofile/mappedphysicalinputnames%28forelementalias%29.md)
  Returns the physical input elements to which the user remaps the given input element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerusercustomizationsdidchangenotification)*