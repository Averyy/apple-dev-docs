# memoryRestartCopy

**Framework**: Foundation  
**Kind**: property

A strategic copy was attempted of an object upon which a quicker copy is now possible.  The caller should retry the copy using vm_object_copy_quickly. This error code is seen only by the kernel.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var memoryRestartCopy: MachError.Code { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/macherror/memoryrestartcopy)*