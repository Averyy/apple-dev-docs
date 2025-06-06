# shared

**Framework**: Swift  
**Kind**: property  
**Required**: Yes

The shared actor instance that will be used to provide mutually-exclusive access to declarations annotated with the given global actor type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static var shared: Self.ActorType { get }
```

#### Discussion

The value of this property must always evaluate to the same actor instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/globalactor/shared)*