# initializeBindings

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

Configures whether Metal initializes the bindings to nil values upon creation of argument table.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var initializeBindings: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL initializeBindings;
```

#### Discussion

The default value of this property is [`false`](../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4argumenttabledescriptor/initializebindings)*