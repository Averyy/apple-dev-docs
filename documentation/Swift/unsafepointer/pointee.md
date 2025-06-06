# pointee

**Framework**: Swift  
**Kind**: property

Accesses the instance referenced by this pointer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var pointee: Pointee { get }
```

#### Discussion

When reading from the `pointee` property, the instance referenced by this pointer must already be initialized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafepointer/pointee)*