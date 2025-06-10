# assign(to:)

**Framework**: Combine  
**Kind**: method

Republishes elements received from a publisher, by assigning them to a property marked as a publisher.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func assign(to published: inout Published<Self.Output>.Publisher)
```

#### Discussion

Use this operator when you want to receive elements from a publisher and republish them through a property marked with the `@Published` attribute. The `assign(to:)` operator manages the life cycle of the subscription, canceling the subscription automatically when the [`Published`](published.md) instance deinitializes. Because of this, the `assign(to:)` operator doesn’t return an [`AnyCancellable`](anycancellable.md) that you’re responsible for like [`assign(to:on:)`](publishers/throttle/assign(to:on:).md) does.

The example below shows a model class that receives elements from an internal [`Timer.TimerPublisher`](https://developer.apple.com/documentation/Foundation/Timer/TimerPublisher), and assigns them to a `@Published` property called `lastUpdated`. Because the `to` parameter has the `inout` keyword, you need to use the `&` operator when calling this method.

```swift
class MyModel: ObservableObject {
    @Published var lastUpdated: Date = Date()
    init() {
         Timer.publish(every: 1.0, on: .main, in: .common)
             .autoconnect()
             .assign(to: &$lastUpdated)
    }
}
```

If you instead implemented `MyModel` with `assign(to: lastUpdated, on: self)`, storing the returned [`AnyCancellable`](anycancellable.md) instance could cause a reference cycle, because the [`Subscribers.Assign`](subscribers/assign.md) subscriber would hold a strong reference to `self`. Using `assign(to:)` solves this problem.

While the `to` parameter uses the `inout` keyword, this method doesn’t replace a reference type passed to it. Instead, this notation indicates that the operator may modify members of the assigned object, as seen in the following example:

```swift
    class MyModel2: ObservableObject {
        @Published var id: Int = 0
    }
    let model2 = MyModel2()
    Just(100).assign(to: &model2.$id)
```

## Parameters

- `published`: A property marked with the   attribute, which receives and republishes all elements received from the upstream publisher.

## See Also

- [func assign<Root>(to: ReferenceWritableKeyPath<Root, Self.Output>, on: Root) -> AnyCancellable](publishers/throttle/assign(to:on:).md)
  Assigns each element from a publisher to a property on an object.
- [func sink(receiveCompletion: (Subscribers.Completion<Self.Failure>) -> Void, receiveValue: (Self.Output) -> Void) -> AnyCancellable](publishers/throttle/sink(receivecompletion:receivevalue:).md)
  Attaches a subscriber with closure-based behavior.
- [func sink(receiveValue: (Self.Output) -> Void) -> AnyCancellable](publishers/throttle/sink(receivevalue:).md)
  Attaches a subscriber with closure-based behavior to a publisher that never fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/throttle/assign(to:))*