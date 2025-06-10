# IntentFile.IntentFileError

**Framework**: App Intents  
**Kind**: enum

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
enum IntentFileError
```

## Topics

### Operators
- [static func == (IntentFile.IntentFileError, IntentFile.IntentFileError) -> Bool](intentfile/intentfileerror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [IntentFile.IntentFileError.failedToLoadData](intentfile/intentfileerror/failedtoloaddata.md)
- [IntentFile.IntentFileError.failedToLoadFile](intentfile/intentfileerror/failedtoloadfile.md)
### Instance Properties
- [var errorCode: Int](intentfile/intentfileerror/errorcode.md)
  The error code within the given domain.
- [var errorUserInfo: [String : Any]](intentfile/intentfileerror/erroruserinfo.md)
  The user-info dictionary.
- [var hashValue: Int](intentfile/intentfileerror/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](intentfile/intentfileerror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static var errorDomain: String](intentfile/intentfileerror/errordomain.md)
  The domain of the error.
### Default Implementations
- [CustomNSError Implementations](intentfile/intentfileerror/customnserror-implementations.md)
- [Equatable Implementations](intentfile/intentfileerror/equatable-implementations.md)
- [Error Implementations](intentfile/intentfileerror/error-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentfile/intentfileerror)*