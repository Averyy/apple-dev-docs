# GenerationID

**Framework**: Foundation Models  
**Kind**: struct

A unique identifier that is stable for the duration of a response, but not across responses.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct GenerationID
```

#### Overview

The framework guarantees a [`GenerationID`](generationid.md) to be both present and stable when you receive it from a [`LanguageModelSession`](languagemodelsession.md). When you create an instance of [`GenerationID`](generationid.md) there is no guarantee an identifier is present or stable.

```swift
@Generable
struct Person: Equatable {
    var name: String
}

struct PeopleView: View {
    @State private var session = LanguageModelSession()
    @State private var people = [Person.PartiallyGenerated]()
    
    var body: some View {
        // A person's name changes as the response is generated,
        // and two people can have the same name, so it's not suitable
        // for use as an id.
        //
        // `GenerationID` receives special treatment and is guaranteed
        // to be both present and stable.
        List {
            // The framework generates each instance with a `GenerationID`.
            ForEach(people, id: \.id) { person in
                Text("Name: \(person.name ?? "")")
            }
        }
        .task {
            do {
                for try await people in session.streamResponse(
                    to: "Who were the first 3 presidents of the US?",
                    generating: [Person].self
                ) {
                    withAnimation {
                        self.people = people.content
                    }
                }
            } catch {
                // Handle the thrown error.
            }
        }
    }
}
```

## Topics

### Creating an identifier
- [init()](generationid/init.md)
  Create a new, unique `GenerationID`.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationid)*