# createContext(forIdentifier:parentContext:parentIdentifierPath:)

**Framework**: ClassKit  
**Kind**: method  
**Required**: Yes

Asks the delegate for a new context with the given identifier for the given parent context.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func createContext(forIdentifier identifier: String, parentContext: CLSContext, parentIdentifierPath: [String]) -> CLSContext?
```

#### Return Value

The new context.

#### Discussion

The framework automatically adds the returned context as a child of the parent context and saves the changes. You only need to create, initialize, and return the new context.

## Parameters

- `identifier`: The identifier of the new context.
- `parentContext`: The parent of the new context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsdatastoredelegate/createcontext(foridentifier:parentcontext:parentidentifierpath:))*