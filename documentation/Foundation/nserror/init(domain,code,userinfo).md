# init(domain:code:userInfo:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an `NSError` object initialized for a given domain and code with a given `userInfo` dictionary.

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
init(domain: String, code: Int, userInfo dict: [String : Any]? = nil)
```

```objc
- (instancetype) initWithDomain:(NSErrorDomain) domain code:(NSInteger) code userInfo:(NSDictionary<NSString *,id> *) dict;
```

#### Return Value

An `NSError` object initialized for `domain` with the specified error `code` and the dictionary of arbitrary data `userInfo`.

#### Discussion

This is the designated initializer for `NSError`.

## Parameters

- `domain`: The error domain—this can be one of the predefined `NSError` domains, or an arbitrary string describing a custom domain. `domain` must not be `nil`. See `Error Domains` for a list of predefined domains.
- `code`: The error code for the error.
- `dict`: The `userInfo` dictionary for the error. `userInfo` may be `nil`.

## See Also

### Related Documentation
- [+ errorWithDomain:code:userInfo:](./errorwithdomain_code_userinfo_.md)
  Creates and initializes an `NSError` object for a given domain and code with a given `userInfo` dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nserror/init(domain:code:userinfo:))*