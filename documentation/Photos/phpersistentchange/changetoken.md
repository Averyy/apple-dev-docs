# changeToken

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

An opaque object that represents the state of Photos library.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var changeToken: PHPersistentChangeToken { get }
```

```objc
@property (nonatomic, readonly) PHPersistentChangeToken * changeToken;
```

## See Also

### Getting the Change Token
- [class PHPersistentChangeToken](../phpersistentchangetoken.md)
  An opaque object that tracks the state of the Photos library between runs, and that you can copy and serialize for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phpersistentchange/changetoken)*