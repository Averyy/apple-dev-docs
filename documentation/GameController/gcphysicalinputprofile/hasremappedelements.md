# hasRemappedElements

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) BOOL hasRemappedElements;
```

## Discussion

If [`true`](../../Swift/true.md), the user remaps one or more elements; otherwise, this property is [`false`](../../Swift/false.md).

## See Also

### Remapping input elements
- [func mappedElementAlias(forPhysicalInputName: String) -> String](./mappedelementalias%28forphysicalinputname%29.md)
  Returns the name of the input element to which the user remaps the given physical element.
- [func mappedPhysicalInputNames(forElementAlias: String) -> Set<String>](./mappedphysicalinputnames%28forelementalias%29.md)
  Returns the physical input elements to which the user remaps the given input element.
- [static let GCControllerUserCustomizationsDidChange: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/gccontrollerusercustomizationsdidchange.md)
  A notification that posts when the user customizes the button mappings or other settings of a controller.
- [GCControllerUserCustomizationsDidChangeNotification](../gccontrollerusercustomizationsdidchangenotification.md)
  A notification that posts when the user customizes the button mappings or other settings of a controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputprofile/hasremappedelements)*