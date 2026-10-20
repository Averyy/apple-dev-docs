# name

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The name associated with the receiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var name: String? { get set }
```

```objc
@property (copy, nullable) NSString * name;
```

#### Discussion

You can use a name string to identify a condition lock within your code. Cocoa also uses this name as part of any error descriptions involving the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconditionlock/name)*