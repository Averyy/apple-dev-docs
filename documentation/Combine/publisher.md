# Publisher

**Framework**: Combine  
**Kind**: protocol

Declares that a type can transmit a sequence of values over time.

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
protocol Publisher<Output, Failure>
```

## Mentions

- [Processing Published Elements with Subscribers](processing-published-elements-with-subscribers.md)
- [Using Combine for Your App’s Asynchronous Code](using-combine-for-your-app-s-asynchronous-code.md)
- [Receiving and Handling Events with Combine](receiving-and-handling-events-with-combine.md)

#### Overview

A publisher delivers elements to one or more [`Subscriber`](subscriber.md) instances. The subscriber’s [`Input`](subscriber/input.md) and [`Failure`](subscriber/failure.md) associated types must match the [`Output`](publisher/output.md) and [`Failure`](publisher/failure.md) types declared by the publisher. The publisher implements the [`receive(subscriber:)`](publisher/receive(subscriber:).md)method to accept a subscriber.

After this, the publisher can call the following methods on the subscriber:

- [`receive(subscription:)`](subscriber/receive(subscription:).md): Acknowledges the subscribe request and returns a [`Subscription`](subscription.md) instance. The subscriber uses the subscription to demand elements from the publisher and can use it to cancel publishing.
- [`receive(_:)`](subscriber/receive(_:).md): Delivers one element from the publisher to the subscriber.
- [`receive(completion:)`](subscriber/receive(completion:).md): Informs the subscriber that publishing has ended, either normally or with an error.

Every `Publisher` must adhere to this contract for downstream subscribers to function correctly.

Extensions on `Publisher` define a wide variety of  that you compose to create sophisticated event-processing chains. Each operator returns a type that implements the [`Publisher`](publisher.md) protocol Most of these types exist as extensions on the [`Publishers`](publishers.md) enumeration. For example, the [`map(_:)`](publisher/map(_:)-99evh.md) operator returns an instance of [`Publishers.Map`](publishers/map.md).

> 💡 **Tip**: A Combine publisher fills a role similar to, but distinct from, the [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) in the Swift standard library. A `Publisher` and an `AsyncSequence` both produce elements over time. However, the pull model in Combine uses a [`Subscriber`](subscriber.md) to request elements from a publisher, while Swift concurrency uses the `for`-`await`-`in` syntax to iterate over elements published by an `AsyncSequence`. Both APIs offer methods to modify the sequence by mapping or filtering elements, while only Combine provides time-based operations like [`debounce(for:scheduler:options:)`](publisher/debounce(for:scheduler:options:).md) and [`throttle(for:scheduler:latest:)`](publisher/throttle(for:scheduler:latest:).md), and combining operations like [`merge(with:)`](publisher/merge(with:)-7fk3a.md) and [`combineLatest(_:_:)`](publisher/combinelatest(_:_:)-1n30g.md). To bridge the two approaches, the property [`values`](publisher/values-1dm9r.md) exposes a publisher’s elements as an `AsyncSequence`, allowing you to iterate over them with `for`-`await`-`in` rather than attaching a [`Subscriber`](subscriber.md).

### Creating Your Own Publishers

Rather than implementing the `Publisher` protocol yourself, you can create your own publisher by using one of several types provided by the Combine framework:

- Use a concrete subclass of [`Subject`](subject.md), such as [`PassthroughSubject`](passthroughsubject.md), to publish values on-demand by calling its [`send(_:)`](subject/send(_:).md) method.
- Use a [`CurrentValueSubject`](currentvaluesubject.md) to publish whenever you update the subject’s underlying value.
- Add the `@Published` annotation to a property of one of your own types. In doing so, the property gains a publisher that emits an event whenever the property’s value changes. See the [`Published`](published.md) type for an example of this approach.

## Topics

### Declaring Publisher Topography
- [associatedtype Output](publisher/output.md)
  The kind of values published by this publisher.
- [associatedtype Failure : Error](publisher/failure.md)
  The kind of errors this publisher might publish.
### Working with Subscribers
- [func receive<S>(subscriber: S)](publisher/receive(subscriber:).md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S)](publisher/subscribe(_:)-4u8kn.md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S) -> AnyCancellable](publisher/subscribe(_:)-3fk20.md)
  Attaches the specified subject to this publisher.
### Mapping Elements
- [func map<T>((Self.Output) -> T) -> Publishers.Map<Self, T>](publisher/map(_:)-99evh.md)
  Transforms all elements from the upstream publisher with a provided closure.
- [func tryMap<T>((Self.Output) throws -> T) -> Publishers.TryMap<Self, T>](publisher/trymap(_:).md)
  Transforms all elements from the upstream publisher with a provided error-throwing closure.
- [func mapError<E>((Self.Failure) -> E) -> Publishers.MapError<Self, E>](publisher/maperror(_:).md)
  Converts any failure from the upstream publisher into a new error.
- [func replaceNil<T>(with: T) -> Publishers.Map<Self, T>](publisher/replacenil(with:).md)
  Replaces nil elements in the stream with the provided element.
- [func scan<T>(T, (T, Self.Output) -> T) -> Publishers.Scan<Self, T>](publisher/scan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [func tryScan<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryScan<Self, T>](publisher/tryscan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to an error-throwing closure along with the last value returned by the closure.
- [func setFailureType<E>(to: E.Type) -> Publishers.SetFailureType<Self, E>](publisher/setfailuretype(to:).md)
  Changes the failure type declared by the upstream publisher.
### Filtering Elements
- [func filter((Self.Output) -> Bool) -> Publishers.Filter<Self>](publisher/filter(_:).md)
  Republishes all elements that match a provided closure.
- [func tryFilter((Self.Output) throws -> Bool) -> Publishers.TryFilter<Self>](publisher/tryfilter(_:).md)
  Republishes all elements that match a provided error-throwing closure.
- [func compactMap<T>((Self.Output) -> T?) -> Publishers.CompactMap<Self, T>](publisher/compactmap(_:).md)
  Calls a closure with each received element and publishes any returned optional that has a value.
- [func tryCompactMap<T>((Self.Output) throws -> T?) -> Publishers.TryCompactMap<Self, T>](publisher/trycompactmap(_:).md)
  Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [func removeDuplicates() -> Publishers.RemoveDuplicates<Self>](publisher/removeduplicates.md)
  Publishes only elements that don’t match the previous element.
- [func removeDuplicates(by: (Self.Output, Self.Output) -> Bool) -> Publishers.RemoveDuplicates<Self>](publisher/removeduplicates(by:).md)
  Publishes only elements that don’t match the previous element, as evaluated by a provided closure.
- [func tryRemoveDuplicates(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryRemoveDuplicates<Self>](publisher/tryremoveduplicates(by:).md)
  Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [func replaceEmpty(with: Self.Output) -> Publishers.ReplaceEmpty<Self>](publisher/replaceempty(with:).md)
  Replaces an empty stream with the provided element.
- [func replaceError(with: Self.Output) -> Publishers.ReplaceError<Self>](publisher/replaceerror(with:).md)
  Replaces any errors in the stream with the provided element.
### Reducing Elements
- [func collect() -> Publishers.Collect<Self>](publisher/collect.md)
  Collects all received elements, and emits a single array of the collection when the upstream publisher finishes.
- [func collect(Int) -> Publishers.CollectByCount<Self>](publisher/collect(_:).md)
  Collects up to the specified number of elements, and then emits a single array of the collection.
- [func collect<S>(Publishers.TimeGroupingStrategy<S>, options: S.SchedulerOptions?) -> Publishers.CollectByTime<Self, S>](publisher/collect(_:options:).md)
  Collects elements by a given time-grouping strategy, and emits a single array of the collection.
- [Publishers.TimeGroupingStrategy](publishers/timegroupingstrategy.md)
  A strategy for collecting received elements.
- [func ignoreOutput() -> Publishers.IgnoreOutput<Self>](publisher/ignoreoutput.md)
  Ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [func reduce<T>(T, (T, Self.Output) -> T) -> Publishers.Reduce<Self, T>](publisher/reduce(_:_:).md)
  Applies a closure that collects each element of a stream and publishes a final result upon completion.
- [func tryReduce<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryReduce<Self, T>](publisher/tryreduce(_:_:).md)
  Applies an error-throwing closure that collects each element of a stream and publishes a final result upon completion.
### Applying Mathematical Operations on Elements
- [func count() -> Publishers.Count<Self>](publisher/count.md)
  Publishes the number of elements received from the upstream publisher.
- [func max() -> Publishers.Comparison<Self>](publisher/max.md)
  Publishes the maximum value received from the upstream publisher, after it finishes.
- [func max(by: (Self.Output, Self.Output) -> Bool) -> Publishers.Comparison<Self>](publisher/max(by:).md)
  Publishes the maximum value received from the upstream publisher, using the provided ordering closure.
- [func tryMax(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](publisher/trymax(by:).md)
  Publishes the maximum value received from the upstream publisher, using the provided error-throwing closure to order the items.
- [func min() -> Publishers.Comparison<Self>](publisher/min.md)
  Publishes the minimum value received from the upstream publisher, after it finishes.
- [func min(by: (Self.Output, Self.Output) -> Bool) -> Publishers.Comparison<Self>](publisher/min(by:).md)
  Publishes the minimum value received from the upstream publisher, after it finishes.
- [func tryMin(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](publisher/trymin(by:).md)
  Publishes the minimum value received from the upstream publisher, using the provided error-throwing closure to order the items.
### Applying Matching Criteria to Elements
- [func contains(Self.Output) -> Publishers.Contains<Self>](publisher/contains(_:).md)
  Publishes a Boolean value upon receiving an element equal to the argument.
- [func contains(where: (Self.Output) -> Bool) -> Publishers.ContainsWhere<Self>](publisher/contains(where:).md)
  Publishes a Boolean value upon receiving an element that satisfies the predicate closure.
- [func tryContains(where: (Self.Output) throws -> Bool) -> Publishers.TryContainsWhere<Self>](publisher/trycontains(where:).md)
  Publishes a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [func allSatisfy((Self.Output) -> Bool) -> Publishers.AllSatisfy<Self>](publisher/allsatisfy(_:).md)
  Publishes a single Boolean value that indicates whether all received elements pass a given predicate.
- [func tryAllSatisfy((Self.Output) throws -> Bool) -> Publishers.TryAllSatisfy<Self>](publisher/tryallsatisfy(_:).md)
  Publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.
### Applying Sequence Operations to Elements
- [func drop<P>(untilOutputFrom: P) -> Publishers.DropUntilOutput<Self, P>](publisher/drop(untiloutputfrom:).md)
  Ignores elements from the upstream publisher until it receives an element from a second publisher.
- [func dropFirst(Int) -> Publishers.Drop<Self>](publisher/dropfirst(_:).md)
  Omits the specified number of elements before republishing subsequent elements.
- [func drop(while: (Self.Output) -> Bool) -> Publishers.DropWhile<Self>](publisher/drop(while:).md)
  Omits elements from the upstream publisher until a given closure returns false, before republishing all remaining elements.
- [func tryDrop(while: (Self.Output) throws -> Bool) -> Publishers.TryDropWhile<Self>](publisher/trydrop(while:).md)
  Omits elements from the upstream publisher until an error-throwing closure returns false, before republishing all remaining elements.
- [func append(Self.Output...) -> Publishers.Concatenate<Self, Publishers.Sequence<[Self.Output], Self.Failure>>](publisher/append(_:)-1qb8d.md)
  Appends a publisher’s output with the specified elements.
- [func append<S>(S) -> Publishers.Concatenate<Self, Publishers.Sequence<S, Self.Failure>>](publisher/append(_:)-69sdn.md)
  Appends a publisher’s output with the specified sequence.
- [func append<P>(P) -> Publishers.Concatenate<Self, P>](publisher/append(_:)-5yh02.md)
  Appends the output of this publisher with the elements emitted by the given publisher.
- [func prepend(Self.Output...) -> Publishers.Concatenate<Publishers.Sequence<[Self.Output], Self.Failure>, Self>](publisher/prepend(_:)-7wk5l.md)
  Prefixes a publisher’s output with the specified values.
- [func prepend<S>(S) -> Publishers.Concatenate<Publishers.Sequence<S, Self.Failure>, Self>](publisher/prepend(_:)-v9sb.md)
  Prefixes a publisher’s output with the specified sequence.
- [func prepend<P>(P) -> Publishers.Concatenate<P, Self>](publisher/prepend(_:)-5dj9c.md)
  Prefixes the output of this publisher with the elements emitted by the given publisher.
- [func prefix(Int) -> Publishers.Output<Self>](publisher/prefix(_:).md)
  Republishes elements up to the specified maximum count.
- [func prefix(while: (Self.Output) -> Bool) -> Publishers.PrefixWhile<Self>](publisher/prefix(while:).md)
  Republishes elements while a predicate closure indicates publishing should continue.
- [func tryPrefix(while: (Self.Output) throws -> Bool) -> Publishers.TryPrefixWhile<Self>](publisher/tryprefix(while:).md)
  Republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [func prefix<P>(untilOutputFrom: P) -> Publishers.PrefixUntilOutput<Self, P>](publisher/prefix(untiloutputfrom:).md)
  Republishes elements until another publisher emits an element.
### Selecting Specific Elements
- [func first() -> Publishers.First<Self>](publisher/first.md)
  Publishes the first element of a stream, then finishes.
- [func first(where: (Self.Output) -> Bool) -> Publishers.FirstWhere<Self>](publisher/first(where:).md)
  Publishes the first element of a stream to satisfy a predicate closure, then finishes normally.
- [func tryFirst(where: (Self.Output) throws -> Bool) -> Publishers.TryFirstWhere<Self>](publisher/tryfirst(where:).md)
  Publishes the first element of a stream to satisfy a throwing predicate closure, then finishes normally.
- [func last() -> Publishers.Last<Self>](publisher/last.md)
  Publishes the last element of a stream, after the stream finishes.
- [func last(where: (Self.Output) -> Bool) -> Publishers.LastWhere<Self>](publisher/last(where:).md)
  Publishes the last element of a stream that satisfies a predicate closure, after upstream finishes.
- [func tryLast(where: (Self.Output) throws -> Bool) -> Publishers.TryLastWhere<Self>](publisher/trylast(where:).md)
  Publishes the last element of a stream that satisfies an error-throwing predicate closure, after the stream finishes.
- [func output(at: Int) -> Publishers.Output<Self>](publisher/output(at:).md)
  Publishes a specific element, indicated by its index in the sequence of published elements.
- [func output<R>(in: R) -> Publishers.Output<Self>](publisher/output(in:).md)
  Publishes elements specified by their range in the sequence of published elements.
### Collecting and Republishing the Latest Elements from Multiple Publishers
- [func combineLatest<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.CombineLatest<Self, P>, T>](publisher/combinelatest(_:_:)-1n30g.md)
  Subscribes to an additional publisher and invokes a closure upon receiving output from either publisher.
- [func combineLatest<P>(P) -> Publishers.CombineLatest<Self, P>](publisher/combinelatest(_:).md)
  Subscribes to an additional publisher and publishes a tuple upon receiving output from either publisher.
- [func combineLatest<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.CombineLatest3<Self, P, Q>, T>](publisher/combinelatest(_:_:_:)-6ekpz.md)
  Subscribes to two additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func combineLatest<P, Q>(P, Q) -> Publishers.CombineLatest3<Self, P, Q>](publisher/combinelatest(_:_:)-5crqg.md)
  Subscribes to two additional publishers and publishes a tuple upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R, T>(P, Q, R, (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.CombineLatest4<Self, P, Q, R>, T>](publisher/combinelatest(_:_:_:_:).md)
  Subscribes to three additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R>(P, Q, R) -> Publishers.CombineLatest4<Self, P, Q, R>](publisher/combinelatest(_:_:_:)-48buc.md)
  Subscribes to three additional publishers and publishes a tuple upon receiving output from any of the publishers.
### Republishing Elements from Multiple Publishers as an Interleaved Stream
- [func merge(with: Self) -> Publishers.MergeMany<Self>](publisher/merge(with:)-7fk3a.md)
  Combines elements from this publisher with those from another publisher of the same type, delivering an interleaved sequence of elements.
- [func merge<P>(with: P) -> Publishers.Merge<Self, P>](publisher/merge(with:)-7qt71.md)
  Combines elements from this publisher with those from another publisher, delivering an interleaved sequence of elements.
- [func merge<B, C>(with: B, C) -> Publishers.Merge3<Self, B, C>](publisher/merge(with:_:).md)
  Combines elements from this publisher with those from two other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D>(with: B, C, D) -> Publishers.Merge4<Self, B, C, D>](publisher/merge(with:_:_:).md)
  Combines elements from this publisher with those from three other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E>(with: B, C, D, E) -> Publishers.Merge5<Self, B, C, D, E>](publisher/merge(with:_:_:_:).md)
  Combines elements from this publisher with those from four other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F>(with: B, C, D, E, F) -> Publishers.Merge6<Self, B, C, D, E, F>](publisher/merge(with:_:_:_:_:).md)
  Combines elements from this publisher with those from five other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F, G>(with: B, C, D, E, F, G) -> Publishers.Merge7<Self, B, C, D, E, F, G>](publisher/merge(with:_:_:_:_:_:).md)
  Combines elements from this publisher with those from six other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F, G, H>(with: B, C, D, E, F, G, H) -> Publishers.Merge8<Self, B, C, D, E, F, G, H>](publisher/merge(with:_:_:_:_:_:_:).md)
  Combines elements from this publisher with those from seven other publishers, delivering an interleaved sequence of elements.
### Collecting and Republishing the Oldest Unconsumed Elements from Multiple Publishers
- [func zip<P>(P) -> Publishers.Zip<Self, P>](publisher/zip(_:).md)
  Combines elements from another publisher and deliver pairs of elements as tuples.
- [func zip<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.Zip<Self, P>, T>](publisher/zip(_:_:)-4xn21.md)
  Combines elements from another publisher and delivers a transformed output.
- [func zip<P, Q>(P, Q) -> Publishers.Zip3<Self, P, Q>](publisher/zip(_:_:)-8d7k7.md)
  Combines elements from two other publishers and delivers groups of elements as tuples.
- [func zip<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.Zip3<Self, P, Q>, T>](publisher/zip(_:_:_:)-9yqi1.md)
  Combines elements from two other publishers and delivers a transformed output.
- [func zip<P, Q, R>(P, Q, R) -> Publishers.Zip4<Self, P, Q, R>](publisher/zip(_:_:_:)-16rcy.md)
  Combines elements from three other publishers and delivers groups of elements as tuples.
- [func zip<P, Q, R, T>(P, Q, R, (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.Zip4<Self, P, Q, R>, T>](publisher/zip(_:_:_:_:).md)
  Combines elements from three other publishers and delivers a transformed output.
### Republishing Elements by Subscribing to New Publishers
- [func flatMap<T, P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](publisher/flatmap(maxpublishers:_:)-3k7z5.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Publishers.SetFailureType<Self, P.Failure>>](publisher/flatmap(maxpublishers:_:)-qxf.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](publisher/flatmap(maxpublishers:_:)-hyb0.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<Publishers.SetFailureType<P, Self.Failure>, Self>](publisher/flatmap(maxpublishers:_:)-4of8w.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func switchToLatest() -> Publishers.SwitchToLatest<Self.Output, Self>](publisher/switchtolatest-453ht.md)
  Republishes elements sent by the most recently received publisher.
- [func switchToLatest() -> Publishers.SwitchToLatest<Self.Output, Publishers.SetFailureType<Self, Self.Output.Failure>>](publisher/switchtolatest-1c51y.md)
  Republishes elements sent by the most recently received publisher.
- [func switchToLatest() -> Publishers.SwitchToLatest<Publishers.SetFailureType<Self.Output, Self.Failure>, Publishers.Map<Self, Publishers.SetFailureType<Self.Output, Self.Failure>>>](publisher/switchtolatest-20v3t.md)
  Republishes elements sent by the most recently received publisher.
- [func switchToLatest() -> Publishers.SwitchToLatest<Self.Output, Self>](publisher/switchtolatest-9eb3r.md)
  Republishes elements sent by the most recently received publisher.
### Handling Errors
- [func assertNoFailure(String, file: StaticString, line: UInt) -> Publishers.AssertNoFailure<Self>](publisher/assertnofailure(_:file:line:).md)
  Raises a fatal error when its upstream publisher fails, and otherwise republishes all received input.
- [func `catch`<P>((Self.Failure) -> P) -> Publishers.Catch<Self, P>](publisher/catch(_:).md)
  Handles errors from an upstream publisher by replacing it with another publisher.
- [func tryCatch<P>((Self.Failure) throws -> P) -> Publishers.TryCatch<Self, P>](publisher/trycatch(_:).md)
  Handles errors from an upstream publisher by either replacing it with another publisher or throwing a new error.
- [func retry(Int) -> Publishers.Retry<Self>](publisher/retry(_:).md)
  Attempts to recreate a failed subscription with the upstream publisher up to the number of times you specify.
### Controlling Timing
- [func measureInterval<S>(using: S, options: S.SchedulerOptions?) -> Publishers.MeasureInterval<Self, S>](publisher/measureinterval(using:options:).md)
  Measures and emits the time interval between events received from an upstream publisher.
- [func debounce<S>(for: S.SchedulerTimeType.Stride, scheduler: S, options: S.SchedulerOptions?) -> Publishers.Debounce<Self, S>](publisher/debounce(for:scheduler:options:).md)
  Publishes elements only after a specified time interval elapses between events.
- [func delay<S>(for: S.SchedulerTimeType.Stride, tolerance: S.SchedulerTimeType.Stride?, scheduler: S, options: S.SchedulerOptions?) -> Publishers.Delay<Self, S>](publisher/delay(for:tolerance:scheduler:options:).md)
  Delays delivery of all output to the downstream receiver by a specified amount of time on a particular scheduler.
- [func throttle<S>(for: S.SchedulerTimeType.Stride, scheduler: S, latest: Bool) -> Publishers.Throttle<Self, S>](publisher/throttle(for:scheduler:latest:).md)
  Publishes either the most-recent or first element published by the upstream publisher in the specified time interval.
- [func timeout<S>(S.SchedulerTimeType.Stride, scheduler: S, options: S.SchedulerOptions?, customError: (() -> Self.Failure)?) -> Publishers.Timeout<Self, S>](publisher/timeout(_:scheduler:options:customerror:).md)
  Terminates publishing if the upstream publisher exceeds the specified time interval without producing an element.
### Encoding and Decoding
- [func encode<Coder>(encoder: Coder) -> Publishers.Encode<Self, Coder>](publisher/encode(encoder:).md)
  Encodes the output from upstream using a specified encoder.
- [func decode<Item, Coder>(type: Item.Type, decoder: Coder) -> Publishers.Decode<Self, Item, Coder>](publisher/decode(type:decoder:).md)
  Decodes the output from the upstream using a specified decoder.
### Identifying Properties with Key Paths
- [func map<T>(KeyPath<Self.Output, T>) -> Publishers.MapKeyPath<Self, T>](publisher/map(_:)-6sm0a.md)
  Publishes the value of a key path.
- [func map<T0, T1>(KeyPath<Self.Output, T0>, KeyPath<Self.Output, T1>) -> Publishers.MapKeyPath2<Self, T0, T1>](publisher/map(_:_:).md)
  Publishes the values of two key paths as a tuple.
- [func map<T0, T1, T2>(KeyPath<Self.Output, T0>, KeyPath<Self.Output, T1>, KeyPath<Self.Output, T2>) -> Publishers.MapKeyPath3<Self, T0, T1, T2>](publisher/map(_:_:_:).md)
  Publishes the values of three key paths as a tuple.
### Working with Multiple Subscribers
- [func multicast<S>(() -> S) -> Publishers.Multicast<Self, S>](publisher/multicast(_:).md)
  Applies a closure to create a subject that delivers elements to subscribers.
- [func multicast<S>(subject: S) -> Publishers.Multicast<Self, S>](publisher/multicast(subject:).md)
  Provides a subject to deliver elements to multiple subscribers.
- [func share() -> Publishers.Share<Self>](publisher/share.md)
  Shares the output of an upstream publisher with multiple subscribers.
### Buffering Elements
- [func buffer(size: Int, prefetch: Publishers.PrefetchStrategy, whenFull: Publishers.BufferingStrategy<Self.Failure>) -> Publishers.Buffer<Self>](publisher/buffer(size:prefetch:whenfull:).md)
  Buffers elements received from an upstream publisher.
- [Publishers.PrefetchStrategy](publishers/prefetchstrategy.md)
  A strategy for filling a buffer.
- [Publishers.BufferingStrategy](publishers/bufferingstrategy.md)
  A strategy that handles exhaustion of a buffer’s capacity.
### Performing Type-Erasure
- [func eraseToAnyPublisher() -> AnyPublisher<Self.Output, Self.Failure>](publisher/erasetoanypublisher.md)
  Wraps this publisher with a type eraser.
### Specifying Schedulers
- [func subscribe<S>(on: S, options: S.SchedulerOptions?) -> Publishers.SubscribeOn<Self, S>](publisher/subscribe(on:options:).md)
  Specifies the scheduler on which to perform subscribe, cancel, and request operations.
- [func receive<S>(on: S, options: S.SchedulerOptions?) -> Publishers.ReceiveOn<Self, S>](publisher/receive(on:options:).md)
  Specifies the scheduler on which to receive elements from the publisher.
### Adding Explicit Connectability
- [func makeConnectable() -> Publishers.MakeConnectable<Self>](publisher/makeconnectable.md)
  Creates a connectable wrapper around the publisher.
### Connecting Simple Subscribers
- [func assign<Root>(to: ReferenceWritableKeyPath<Root, Self.Output>, on: Root) -> AnyCancellable](publisher/assign(to:on:).md)
  Assigns each element from a publisher to a property on an object.
- [func assign(to: inout Published<Self.Output>.Publisher)](publisher/assign(to:).md)
  Republishes elements received from a publisher, by assigning them to a property marked as a publisher.
- [func sink(receiveCompletion: (Subscribers.Completion<Self.Failure>) -> Void, receiveValue: (Self.Output) -> Void) -> AnyCancellable](publisher/sink(receivecompletion:receivevalue:).md)
  Attaches a subscriber with closure-based behavior.
- [func sink(receiveValue: (Self.Output) -> Void) -> AnyCancellable](publisher/sink(receivevalue:).md)
  Attaches a subscriber with closure-based behavior to a publisher that never fails.
### Accessing Elements Asynchronously
- [var values: AsyncPublisher<Self>](publisher/values-1dm9r.md)
  The elements produced by the publisher, as an asynchronous sequence.
- [var values: AsyncThrowingPublisher<Self>](publisher/values-v7nz.md)
  The elements produced by the publisher, as a throwing asynchronous sequence.
### Debugging
- [func breakpoint(receiveSubscription: ((any Subscription) -> Bool)?, receiveOutput: ((Self.Output) -> Bool)?, receiveCompletion: ((Subscribers.Completion<Self.Failure>) -> Bool)?) -> Publishers.Breakpoint<Self>](publisher/breakpoint(receivesubscription:receiveoutput:receivecompletion:).md)
  Raises a debugger signal when a provided closure needs to stop the process in the debugger.
- [func breakpointOnError() -> Publishers.Breakpoint<Self>](publisher/breakpointonerror.md)
  Raises a debugger signal upon receiving a failure.
- [func handleEvents(receiveSubscription: ((any Subscription) -> Void)?, receiveOutput: ((Self.Output) -> Void)?, receiveCompletion: ((Subscribers.Completion<Self.Failure>) -> Void)?, receiveCancel: (() -> Void)?, receiveRequest: ((Subscribers.Demand) -> Void)?) -> Publishers.HandleEvents<Self>](publisher/handleevents(receivesubscription:receiveoutput:receivecompletion:receivecancel:receiverequest:).md)
  Performs the specified closures when publisher events occur.
- [func print(String, to: (any TextOutputStream)?) -> Publishers.Print<Self>](publisher/print(_:to:).md)
  Prints log messages for all publishing events.

## Relationships

### Inherited By
- [ConnectablePublisher](connectablepublisher.md)
- [Subject](subject.md)
### Conforming Types
- [AnyPublisher](anypublisher.md)
- [CurrentValueSubject](currentvaluesubject.md)
- [Deferred](deferred.md)
- [Empty](empty.md)
- [Fail](fail.md)
- [Future](future.md)
- [Just](just.md)
- [ObservableObjectPublisher](observableobjectpublisher.md)
- [PassthroughSubject](passthroughsubject.md)
- [Published.Publisher](published/publisher.md)
- [Publishers.AllSatisfy](publishers/allsatisfy.md)
- [Publishers.AssertNoFailure](publishers/assertnofailure.md)
- [Publishers.Autoconnect](publishers/autoconnect.md)
- [Publishers.Breakpoint](publishers/breakpoint.md)
- [Publishers.Buffer](publishers/buffer.md)
- [Publishers.Catch](publishers/catch.md)
- [Publishers.Collect](publishers/collect.md)
- [Publishers.CollectByCount](publishers/collectbycount.md)
- [Publishers.CollectByTime](publishers/collectbytime.md)
- [Publishers.CombineLatest](publishers/combinelatest.md)
- [Publishers.CombineLatest3](publishers/combinelatest3.md)
- [Publishers.CombineLatest4](publishers/combinelatest4.md)
- [Publishers.CompactMap](publishers/compactmap.md)
- [Publishers.Comparison](publishers/comparison.md)
- [Publishers.Concatenate](publishers/concatenate.md)
- [Publishers.Contains](publishers/contains.md)
- [Publishers.ContainsWhere](publishers/containswhere.md)
- [Publishers.Count](publishers/count.md)
- [Publishers.Debounce](publishers/debounce.md)
- [Publishers.Decode](publishers/decode.md)
- [Publishers.Delay](publishers/delay.md)
- [Publishers.Drop](publishers/drop.md)
- [Publishers.DropUntilOutput](publishers/dropuntiloutput.md)
- [Publishers.DropWhile](publishers/dropwhile.md)
- [Publishers.Encode](publishers/encode.md)
- [Publishers.Filter](publishers/filter.md)
- [Publishers.First](publishers/first.md)
- [Publishers.FirstWhere](publishers/firstwhere.md)
- [Publishers.FlatMap](publishers/flatmap.md)
- [Publishers.HandleEvents](publishers/handleevents.md)
- [Publishers.IgnoreOutput](publishers/ignoreoutput.md)
- [Publishers.Last](publishers/last.md)
- [Publishers.LastWhere](publishers/lastwhere.md)
- [Publishers.MakeConnectable](publishers/makeconnectable.md)
- [Publishers.Map](publishers/map.md)
- [Publishers.MapError](publishers/maperror.md)
- [Publishers.MapKeyPath](publishers/mapkeypath.md)
- [Publishers.MapKeyPath2](publishers/mapkeypath2.md)
- [Publishers.MapKeyPath3](publishers/mapkeypath3.md)
- [Publishers.MeasureInterval](publishers/measureinterval.md)
- [Publishers.Merge](publishers/merge.md)
- [Publishers.Merge3](publishers/merge3.md)
- [Publishers.Merge4](publishers/merge4.md)
- [Publishers.Merge5](publishers/merge5.md)
- [Publishers.Merge6](publishers/merge6.md)
- [Publishers.Merge7](publishers/merge7.md)
- [Publishers.Merge8](publishers/merge8.md)
- [Publishers.MergeMany](publishers/mergemany.md)
- [Publishers.Multicast](publishers/multicast.md)
- [Publishers.Output](publishers/output.md)
- [Publishers.PrefixUntilOutput](publishers/prefixuntiloutput.md)
- [Publishers.PrefixWhile](publishers/prefixwhile.md)
- [Publishers.Print](publishers/print.md)
- [Publishers.ReceiveOn](publishers/receiveon.md)
- [Publishers.Reduce](publishers/reduce.md)
- [Publishers.RemoveDuplicates](publishers/removeduplicates.md)
- [Publishers.ReplaceEmpty](publishers/replaceempty.md)
- [Publishers.ReplaceError](publishers/replaceerror.md)
- [Publishers.Retry](publishers/retry.md)
- [Publishers.Scan](publishers/scan.md)
- [Publishers.Sequence](publishers/sequence.md)
- [Publishers.SetFailureType](publishers/setfailuretype.md)
- [Publishers.Share](publishers/share.md)
- [Publishers.SubscribeOn](publishers/subscribeon.md)
- [Publishers.SwitchToLatest](publishers/switchtolatest.md)
- [Publishers.Throttle](publishers/throttle.md)
- [Publishers.Timeout](publishers/timeout.md)
- [Publishers.TryAllSatisfy](publishers/tryallsatisfy.md)
- [Publishers.TryCatch](publishers/trycatch.md)
- [Publishers.TryCompactMap](publishers/trycompactmap.md)
- [Publishers.TryComparison](publishers/trycomparison.md)
- [Publishers.TryContainsWhere](publishers/trycontainswhere.md)
- [Publishers.TryDropWhile](publishers/trydropwhile.md)
- [Publishers.TryFilter](publishers/tryfilter.md)
- [Publishers.TryFirstWhere](publishers/tryfirstwhere.md)
- [Publishers.TryLastWhere](publishers/trylastwhere.md)
- [Publishers.TryMap](publishers/trymap.md)
- [Publishers.TryPrefixWhile](publishers/tryprefixwhile.md)
- [Publishers.TryReduce](publishers/tryreduce.md)
- [Publishers.TryRemoveDuplicates](publishers/tryremoveduplicates.md)
- [Publishers.TryScan](publishers/tryscan.md)
- [Publishers.Zip](publishers/zip.md)
- [Publishers.Zip3](publishers/zip3.md)
- [Publishers.Zip4](publishers/zip4.md)
- [Record](record.md)

## See Also

- [enum Publishers](publishers.md)
  A namespace for types that serve as publishers.
- [struct AnyPublisher](anypublisher.md)
  A publisher that performs type erasure by wrapping another publisher.
- [struct Published](published.md)
  A type that publishes a property marked with an attribute.
- [protocol Cancellable](cancellable.md)
  A protocol indicating that an activity or action supports cancellation.
- [class AnyCancellable](anycancellable.md)
  A type-erasing cancellable object that executes a provided closure when canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher)*