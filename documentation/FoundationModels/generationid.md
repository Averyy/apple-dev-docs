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
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct GenerationID
```

#### Overview

The framework guarantees a `GenerationID` to be both present and stable when you receive it from a [`LanguageModelSession`](languagemodelsession.md). When you create an instance of `GenerationID` there is no guarantee an identifier is present or stable.

```swift
@Generable struct Person: Equatable {
    var id: GenerationID
    var name: String
}

struct PeopleView: View {
    @State private var session = LanguageModelSession()
    @State private var people = [Person.PartiallyGenerated]()

    var body: some View {
        // A person's name changes as the response is generated,
        // and two people can have the same name, so it is not suitable
        // for use as an id.
        //
        // `GenerationID` receives special treatment and is guaranteed
        // to be both present and stable.
        List {
            ForEach(people) { person in
                Text("Name: \(person.name)")
            }
        }
        .task {
            do {
                for try! await people in stream.streamResponse(
                    to: "Who were the first 3 presidents of the US?",
                    generating: [Person].self
                ) {
                    withAnimation {
                        self.people = people
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
  Creates a unique identifier.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var id: GenerationID?](generatedcontent/id.md)
  A unique id that is stable for the duration of a generated response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationid)*