# components

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var components: [any MDLComponent] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<id<MDLComponent>> * components;
```

## See Also

### Managing Rendering Intent
- [var hidden: Bool](./hidden.md)
  A Boolean value indicating whether this object should be used in rendering.
- [var instance: MDLObject?](./instance.md)
  The primary object, if applicable, of which this object is an instance.
- [var path: String](./path.md)
  A path that identifies the object in an asset’s object hierarchy using object names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlobject/components)*