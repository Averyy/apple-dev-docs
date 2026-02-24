# null

**Framework**: Foundation Models  
**Kind**: property

Creates a null schema.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)

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