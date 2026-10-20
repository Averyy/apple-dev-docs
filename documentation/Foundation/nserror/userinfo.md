# userInfo

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The user info dictionary.

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
var userInfo: [String : Any] { get }
```

```objc
@property (copy, readonly) NSDictionary<NSString *,id> * userInfo;
```

#### Discussion

If the user info dictionary has not been set, this property is `nil`.

On macOS 10.8 or later, if the user info dictionary has not been set, this property returns an empty dictionary.

## See Also

### Related Documentation
- [var localizedDescription: String](./localizeddescription.md)
  A string containing the localized description of the error.
### Getting Error Properties
- [var code: Int](./code.md)
  The error code.
- [var domain: String](./domain.md)
  A string containing the error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nserror/userinfo)*