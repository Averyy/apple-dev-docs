# CLSErrorUserInfoKey

**Framework**: ClassKit  
**Kind**: struct  
**Role**: Structure

Keys that appear in the user info dictionary in errors that ClassKit creates.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct CLSErrorUserInfoKey
```

```c
typedef NSString * CLSErrorUserInfoKey;
```

## Topics

### Keys
- [static let objectKey: CLSErrorUserInfoKey](./clserroruserinfokey/objectkey.md)
  A key whose value is the object that caused the error.
- [static let successfulObjectsKey: CLSErrorUserInfoKey](./clserroruserinfokey/successfulobjectskey.md)
- [static let underlyingErrorsKey: CLSErrorUserInfoKey](./clserroruserinfokey/underlyingerrorskey.md)
  A key whose value is the array of errors that contributed to this error.
### Initializers
- [init(String)](./clserroruserinfokey/init%28_%29.md)
  Initializes the key.
- [init(rawValue: String)](./clserroruserinfokey/init%28rawvalue%29.md)
  Initializes the key with a value.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Errors
- [struct CLSError](./clserror.md)
  Errors issued by ClassKit.
- [let CLSErrorCodeDomain: String](./clserrorcodedomain.md)
  The error domain that ClassKit uses when issuing errors.
- [CLSError.Code](./clserror/code.md)
  Error codes that ClassKit issues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clserroruserinfokey)*