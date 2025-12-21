# accessInstanceVariablesDirectly

**Framework**: Objective-C Runtime  
**Kind**: property

Returns a Boolean value that indicates whether the key-value coding methods should access the corresponding instance variable directly on finding no accessor method for a property.

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
class var accessInstanceVariablesDirectly: Bool { get }
```

#### Return Value

[`YES`](yes.md) if the key-value coding methods should access the corresponding instance variable directly on finding no accessor method for a property, otherwise [`NO`](no.md).

#### Discussion

The default returns [`YES`](yes.md). Subclasses can override it to return [`NO`](no.md), in which case the key-value coding methods won’t access instance variables.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessinstancevariablesdirectly)*