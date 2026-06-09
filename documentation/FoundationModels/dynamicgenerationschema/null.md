# null

**Framework**: Foundation Models  
**Kind**: property

Creates a null schema.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+
- watchOS 27.0+ (Beta)

## Declaration

```swift
static var null: DynamicGenerationSchema { get }
```

#### Discussion

You can use null schemas as a way to express types that cannot be absent, but may have an empty value.

```None
let person = DynamicGenerationSchema(
    name: "Person",
    properties: []
        DynamicGenerationSchema.Property(
          name: "fullName",
          schema: DynamicGenerationSchema(type: String.self)
        )
    ]
)

let nullablePerson = DynamicGenerationSchema(
  name: "NullablePerson",
  anyOf: [person, .null]
)

let schema = try GenerationSchema(root: nullablePerson, dependencies: [])
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicgenerationschema/null)*