# hasRemappedElements

**Framework**: Game Controller  
**Kind**: property

A Boolean value that indicates whether the user remaps elements in this profile.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var hasRemappedElements: Bool { get }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), the user remaps one or more elements; otherwise, this property is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func mappedElementAlias(forPhysicalInputName: String) -> String](gcphysicalinputprofile/mappedelementalias(forphysicalinputname:).md)
  Returns the name of the input element to which the user remaps the given physical element.
- [func mappedPhysicalInputNames(forElementAlias: String) -> Set<String>](gcphysicalinputprofile/mappedphysicalinputnames(forelementalias:).md)
  Returns the physical input elements to which the user remaps the given input element.
- [static let GCControllerUserCustomizationsDidChange: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GCControllerUserCustomizationsDidChange.md)
  A notification that posts when the user customizes the button mappings or other settings of a controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputprofile/hasremappedelements)*