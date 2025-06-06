# eraseToAnyPublisher()

**Framework**: RealityKit  
**Kind**: method

Wraps this publisher with a type eraser.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
func eraseToAnyPublisher() -> AnyPublisher<Self.Output, Self.Failure>
```

#### Return Value

An `AnyPublisher` wrapping this publisher.

#### Discussion

Use `Publisher/eraseToAnyPublisher()` to expose an instance of `AnyPublisher` to the downstream subscriber, rather than this publisher’s actual type. This form of  preserves abstraction across API boundaries, such as different modules. When you expose your publishers as the `AnyPublisher` type, you can change the underlying implementation over time without affecting existing clients.

The following example shows two types that each have a `publisher` property. `TypeWithSubject` exposes this property as its actual type, `PassthroughSubject`, while `TypeWithErasedSubject` uses `Publisher/eraseToAnyPublisher()` to expose it as an `AnyPublisher`. As seen in the output, a caller from another module can access `TypeWithSubject.publisher` as its native type. This means you can’t change your publisher to a different type without breaking the caller. By comparison, `TypeWithErasedSubject.publisher` appears to callers as an `AnyPublisher`, so you can change the underlying publisher type at will.

```None
public class TypeWithSubject {
    public let publisher: some Publisher = PassthroughSubject<Int,Never>()
}
public class TypeWithErasedSubject {
    public let publisher: some Publisher = PassthroughSubject<Int,Never>()
        .eraseToAnyPublisher()
}

// In another module:
let nonErased = TypeWithSubject()
if let subject = nonErased.publisher as? PassthroughSubject<Int,Never> {
    print("Successfully cast nonErased.publisher.")
}
let erased = TypeWithErasedSubject()
if let subject = erased.publisher as? PassthroughSubject<Int,Never> {
    print("Successfully cast erased.publisher.")
}

// Prints "Successfully cast nonErased.publisher."
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/loadrequest/erasetoanypublisher())*