# code

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The error code.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var code: Int { get }
```

```objc
@property (readonly) NSInteger code;
```

## Discussion

Note that errors are domain-specific.

## See Also

### Related Documentation
- [var localizedDescription: String](./localizeddescription.md)
  A string containing the localized description of the error.
### Getting Error Properties
- [var domain: String](./domain.md)
  A string containing the error domain.
- [var userInfo: [String : Any]](./userinfo.md)
  The user info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nserror/code)*