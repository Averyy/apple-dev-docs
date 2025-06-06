# mappedPhysicalInputNames(forElementAlias:)

**Framework**: Game Controller  
**Kind**: method

Returns the physical input elements to which the user remaps the given input element.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func mappedPhysicalInputNames(forElementAlias elementAlias: String) -> Set<String>
```

#### Return Value

The names of the physical input element to which the user remaps the given element.

#### Discussion

For example, if the user maps a physical press of A button , B button, and X button to button B, then passing [`GCInputButtonB`](gcinputbuttonb-6z361.md) returns a set that contains [`GCInputButtonA`](gcinputbuttona-8z15w.md), [`GCInputButtonB`](gcinputbuttonb-6z361.md), and [`GCInputButtonX`](gcinputbuttonx-32i2z.md).

## Parameters

- `elementAlias`: The name of the input element too which physical input elements remap. For possible values, see  .

## See Also

- [var hasRemappedElements: Bool](gcphysicalinputprofile/hasremappedelements.md)
  A Boolean value that indicates whether the user remaps elements in this profile.
- [func mappedElementAlias(forPhysicalInputName: String) -> String](gcphysicalinputprofile/mappedelementalias(forphysicalinputname:).md)
  Returns the name of the input element to which the user remaps the given physical element.
- [static let GCControllerUserCustomizationsDidChange: NSNotification.Name](../foundation/nsnotification/name/4066959-gccontrollerusercustomizationsdi.md)
  A notification that posts when the user customizes the button mappings or other settings of a controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputprofile/mappedphysicalinputnames(forelementalias:))*