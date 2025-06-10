# mappedElementAlias(forPhysicalInputName:)

**Framework**: Game Controller  
**Kind**: method

Returns the name of the input element to which the user remaps the given physical element.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func mappedElementAlias(forPhysicalInputName inputName: String) -> String
```

#### Return Value

The name of the input element to which the user remaps the physical element, or `nil` if the user doesn’t remap the physical element.

#### Discussion

Use this method to get the alias for an input element. For example, if the user remaps a physical press of the controller’s A button to button B, then passing [`GCInputButtonA`](gcinputbuttona-8z15w.md) to this method returns [`GCInputButtonB`](gcinputbuttonb-6z361.md).

## Parameters

- `inputName`: The name of the physical element. For possible values, see  .

## See Also

- [var hasRemappedElements: Bool](gcphysicalinputprofile/hasremappedelements.md)
  A Boolean value that indicates whether the user remaps elements in this profile.
- [func mappedPhysicalInputNames(forElementAlias: String) -> Set<String>](gcphysicalinputprofile/mappedphysicalinputnames(forelementalias:).md)
  Returns the physical input elements to which the user remaps the given input element.
- [static let GCControllerUserCustomizationsDidChange: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GCControllerUserCustomizationsDidChange.md)
  A notification that posts when the user customizes the button mappings or other settings of a controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputprofile/mappedelementalias(forphysicalinputname:))*