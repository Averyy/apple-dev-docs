# displayRepresentation(with:)

**Framework**: App Intents  
**Kind**: method  
**Required**: Yes

Asynchronous method to retrieve the DisplayRepresentation with the requested components.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func displayRepresentation(with components: DisplayRepresentation.Components) async -> DisplayRepresentation
```

#### Discussion

Override this method to provide the display representation and populate its properties depending on the components requested. The default value is the existing value of the display representation in its entirety.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/instancedisplayrepresentable/displayrepresentation(with:))*