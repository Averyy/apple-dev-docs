# descriptor

**Framework**: Foundation  
**Kind**: property

Returns an Apple event descriptor that represents the receiver.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@NSCopying
var descriptor: NSAppleEventDescriptor? { get }
```

#### Return Value

An Apple event descriptor of type `typeObjectSpecifier`.

#### Discussion

If the receiver was created with [`init(descriptor:)`](nsscriptobjectspecifier/init(descriptor:).md), the passed-in descriptor is returned. Otherwise, a new descriptor is created and returned, autoreleased.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/descriptor)*