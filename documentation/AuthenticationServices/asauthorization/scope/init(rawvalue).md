# init(rawValue:)

**Framework**: Authentication Services  
**Kind**: init  
**Role**: Initializer

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
init(rawValue: String)
```

#### Discussion

Typically you use one of the predefined scopes, like [`email`](./email.md), instead of initializing one from a string.

## Parameters

- `rawValue`: The name of the scope.

## See Also

### Creating a Scope
- [init(String)](./init%28_%29.md)
  Creates a scope from the given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorization/scope/init(rawvalue:))*