# bug(_:id:_:)

**Framework**: Swift Testing  
**Kind**: method

Constructs a bug to track with a test.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
static func bug(_ url: String? = nil, id: some Numeric, _ title: Comment? = nil) -> Self
```

#### Return Value

An instance of [`Bug`](bug.md) that represents the specified bug.

## Parameters

- `url`: A URL that refers to this bug in the associated bug-tracking   system.
- `id`: The unique identifier of this bug in its associated bug-tracking   system.
- `title`: Optionally, the human-readable title of the bug.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/bug/bug(_:id:_:)-9jvpc)*