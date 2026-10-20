# descriptor

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns an Apple event descriptor that represents the receiver.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@NSCopying
var descriptor: NSAppleEventDescriptor? { get }
```

```objc
@property (copy, readonly, nullable) NSAppleEventDescriptor * descriptor;
```

#### Return Value

An Apple event descriptor of type `typeObjectSpecifier`.

#### Discussion

If the receiver was created with [`init(descriptor:)`](./init%28descriptor%29.md), the passed-in descriptor is returned. Otherwise, a new descriptor is created and returned, autoreleased.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/descriptor)*