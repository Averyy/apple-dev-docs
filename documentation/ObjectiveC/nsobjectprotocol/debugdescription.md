# debugDescription

**Framework**: Objective-C Runtime  
**Kind**: property

A textual representation of the receiver to use with a debugger.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
optional var debugDescription: String { get }
```

#### Return Value

A string that describes the object for debugging purposes.

#### Discussion

The debugger’s `po` command uses this property to create a textual representation of the object suitable for display in the debugger. The default implemention returns the same value as [`description`](nsobjectprotocol/description.md). Override either property to provide custom object descriptions.

## See Also

- [var description: String](nsobjectprotocol/description.md)
  A textual representation of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/debugdescription)*