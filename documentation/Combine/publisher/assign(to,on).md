# assign(to:on:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

Assigns each element from a publisher to a property on an object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func assign<Root>(to keyPath: ReferenceWritableKeyPath<Root, Self.Output>, on object: Root) -> AnyCancellable
```

Available when `Failure` is `Never`.

## Mentions

- [Receiving and Handling Events with Combine](../receiving-and-handling-events-with-combine.md)
- [Processing Published Elements with Subscribers](../processing-published-elements-with-subscribers.md)
- [Replacing Foundation Timers with Timer Publishers](../replacing-foundation-timers-with-timer-publishers.md)

#### Return Value

An [`AnyCancellable`](../anycancellable.md) instance. Call [`cancel()`](../cancellable/cancel%28%29.md) on this instance when you no longer want the publisher to automatically assign the property. Deinitializing this instance will also cancel automatic assignment.

#### Discussion

Use the [`assign(to:on:)`](./assign%28to,on%29.md) subscriber when you want to set a given property each time a publisher produces a value.

In this example, the [`assign(to:on:)`](./assign%28to,on%29.md) sets the value of the `anInt` property on an instance of `MyClass`:

```swift
class MyClass {
    var anInt: Int = 0 {
        didSet {
            print("anInt was set to: \(anInt)", terminator: "; ")
        }
    }
}

var myObject = MyClass()
let myRange = (0...2)
cancellable = myRange.publisher
    .assign(to: \.anInt, on: myObject)

// Prints: "anInt was set to: 0; anInt was set to: 1; anInt was set to: 2"
```

> ❗ **Important**: The [`Subscribers.Assign`](../subscribers/assign.md) instance created by this operator maintains a strong reference to `object`, and sets it to `nil` when the upstream publisher completes (either normally or with an error).

## Parameters

- `keyPath`: A key path that indicates the property to assign. See [Key-Path Expression](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/Expressions.html#//apple_ref/doc/uid/TP40014097-CH32-ID563) in *The Swift Programming Language* to learn how to use key paths to specify a property of an object.
- `object`: The object that contains the property. The subscriber assigns the object’s property every time it receives a new value.

## See Also

### Connecting simple subscribers
- [func assign(to: inout Published<Self.Output>.Publisher)](./assign%28to%29.md)
  Republishes elements received from a publisher, by assigning them to a property marked as a publisher.
- [func sink(receiveCompletion: (Subscribers.Completion<Self.Failure>) -> Void, receiveValue: (Self.Output) -> Void) -> AnyCancellable](./sink%28receivecompletion,receivevalue%29.md)
  Attaches a subscriber with closure-based behavior.
- [func sink(receiveValue: (Self.Output) -> Void) -> AnyCancellable](./sink%28receivevalue%29.md)
  Attaches a subscriber with closure-based behavior to a publisher that never fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/assign(to:on:))*