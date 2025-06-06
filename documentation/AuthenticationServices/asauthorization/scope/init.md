# init(_:)

**Framework**: Authentication Services  
**Kind**: init

Creates a scope from the given string.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(_ rawValue: String)
```

#### Discussion

Typically you use one of the predefined scopes, like [`email`](asauthorization/scope/email.md), instead of initializing one from a string.

## Parameters

- `rawValue`: The name of the scope.

## See Also

- [init(rawValue: String)](asauthorization/scope/init(rawvalue:).md)
  Creates a scope from the given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorization/scope/init(_:))*