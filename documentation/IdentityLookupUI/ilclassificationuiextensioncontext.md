# ILClassificationUIExtensionContext

**Framework**: IdentityLookupUI  
**Kind**: class  
**Role**: Class

An object that manages the state of the current request.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
class ILClassificationUIExtensionContext
```

```objc
@interface ILClassificationUIExtensionContext : NSExtensionContext
```

## Topics

### Readying the Response
- [var isReadyForClassificationResponse: Bool](./ilclassificationuiextensioncontext/isreadyforclassificationresponse.md)
  A Boolean value that determines whether the extension has enough information to complete the report.

## Relationships

### Inherits From
- [NSExtensionContext](../Foundation/nsextensioncontext.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing the Request
- [var extensionContext: ILClassificationUIExtensionContext](./ilclassificationuiextensionviewcontroller/extensioncontext.md)
  The context for the current request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookupui/ilclassificationuiextensioncontext)*