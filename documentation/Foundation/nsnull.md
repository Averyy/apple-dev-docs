# NSNull

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A singleton object used to represent null values in collection objects that don’t allow `nil` values.

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
class NSNull
```

```objc
@interface NSNull : NSObject
```

## Mentions

- [Implementing Handoff in Your App](./implementing-handoff-in-your-app.md)

## Overview

[`NSNull`](./nsnull.md) is “toll-free bridged” with its Core Foundation counterpart, [`CFNull`](../CoreFoundation/cfnull.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

## Topics

### Initializers
- [init?(coder: NSCoder)](./nsnull/init%28coder%29.md)
### Obtaining an instance
- [+ null](./nsnull/null.md)
  Returns the singleton instance of `NSNull`.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CAAction](../QuartzCore/caaction.md)
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Special Semantic Values
- [let NSNotFound: Int](./nsnotfound-9t5v2.md)
- [var NSNotFound: Int](./nsnotfound-4qp9h.md)
  A value indicating that a requested item couldn’t be found or doesn’t exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnull)*