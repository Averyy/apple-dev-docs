# Publisher Operators

**Framework**: Combine

Methods that create downstream publishers or subscribers to act on the elements they receive.

#### Overview

Use operators to assemble a chain of republishers, optionally ending with a subscriber, that processes elements produced by upstream publishers. Each operator creates and configures an instance of a [`Publisher`](publisher.md) or [`Subscriber`](subscriber.md), and subscribes it to the publisher that you call the method on.

In the following example, a sequence publisher emits the integers 1, 2, 3, 4, and 5. A [`filter(_:)`](publisher/filter(_:).md) operator creates a [`Publishers.Filter`](publishers/filter.md) publisher to only republish even values. A second operator creates a [`Subscribers.Sink`](subscribers/sink.md) subscriber to print out each value received. The sink subscriber automatically subscribes to the filter publisher, at which point the filter publisher subscribes to its upstream publisher, the sequence publisher.

```swift
let cancellable = [1, 2, 3, 4, 5].publisher
    .filter {
        $0 % 2 == 0
    }
    .sink {
        print ("Even number: \($0)")
    }
// Prints:
// Even number: 2
// Even number: 4
```

## Topics

### Working with Subscribers
- [func receive<S>(subscriber: S)](just/receive(subscriber:).md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S)](just/subscribe(_:)-3svzx.md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S) -> AnyCancellable](just/subscribe(_:)-3p4s7.md)
  Attaches the specified subject to this publisher.
### Mapping Elements
- [func map<T>((Output) -> T) -> Just<T>](just/map(_:).md)
- [func tryMap<T>((Output) throws -> T) -> Result<T, any Error>.Publisher](just/trymap(_:).md)
- [func mapError<E>((Just<Output>.Failure) -> E) -> Result<Output, E>.Publisher](just/maperror(_:).md)
- [func replaceNil<T>(with: T) -> Publishers.Map<Self, T>](just/replacenil(with:).md)
  Replaces nil elements in the stream with the provided element.
- [func scan<T>(T, (T, Output) -> T) -> Result<T, Just<Output>.Failure>.Publisher](just/scan(_:_:).md)
- [func tryScan<T>(T, (T, Output) throws -> T) -> Result<T, any Error>.Publisher](just/tryscan(_:_:).md)
- [func setFailureType<E>(to: E.Type) -> Result<Output, E>.Publisher](just/setfailuretype(to:).md)
### Filtering Elements
- [func filter((Output) -> Bool) -> Optional<Output>.Publisher](just/filter(_:).md)
- [func tryFilter((Self.Output) throws -> Bool) -> Publishers.TryFilter<Self>](just/tryfilter(_:).md)
  Republishes all elements that match a provided error-throwing closure.
- [func compactMap<T>((Output) -> T?) -> Optional<T>.Publisher](just/compactmap(_:).md)
- [func tryCompactMap<T>((Self.Output) throws -> T?) -> Publishers.TryCompactMap<Self, T>](just/trycompactmap(_:).md)
  Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [func removeDuplicates() -> Just<Output>](just/removeduplicates.md)
- [func removeDuplicates(by: (Output, Output) -> Bool) -> Just<Output>](just/removeduplicates(by:).md)
- [func tryRemoveDuplicates(by: (Output, Output) throws -> Bool) -> Result<Output, any Error>.Publisher](just/tryremoveduplicates(by:).md)
- [func replaceEmpty(with: Output) -> Just<Output>](just/replaceempty(with:).md)
- [func replaceError(with: Output) -> Just<Output>](just/replaceerror(with:).md)
### Reducing Elements
- [func collect() -> Just<[Output]>](just/collect.md)
- [func collect(Int) -> Publishers.CollectByCount<Self>](just/collect(_:).md)
  Collects up to the specified number of elements, and then emits a single array of the collection.
- [func collect<S>(Publishers.TimeGroupingStrategy<S>, options: S.SchedulerOptions?) -> Publishers.CollectByTime<Self, S>](just/collect(_:options:).md)
  Collects elements by a given time-grouping strategy, and emits a single array of the collection.
- [func ignoreOutput() -> Empty<Output, Just<Output>.Failure>](just/ignoreoutput.md)
- [func reduce<T>(T, (T, Output) -> T) -> Result<T, Just<Output>.Failure>.Publisher](just/reduce(_:_:).md)
- [func tryReduce<T>(T, (T, Output) throws -> T) -> Result<T, any Error>.Publisher](just/tryreduce(_:_:).md)
### Applying Mathematical Operations on Elements
- [func count() -> Just<Int>](just/count.md)
- [func max() -> Just<Output>](just/max.md)
- [func max(by: (Output, Output) -> Bool) -> Just<Output>](just/max(by:).md)
- [func tryMax(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](just/trymax(by:).md)
  Publishes the maximum value received from the upstream publisher, using the provided error-throwing closure to order the items.
- [func min() -> Just<Output>](just/min.md)
- [func min(by: (Output, Output) -> Bool) -> Just<Output>](just/min(by:).md)
- [func tryMin(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](just/trymin(by:).md)
  Publishes the minimum value received from the upstream publisher, using the provided error-throwing closure to order the items.
### Applying Matching Criteria to Elements
- [func contains(Output) -> Just<Bool>](just/contains(_:).md)
- [func contains(where: (Output) -> Bool) -> Just<Bool>](just/contains(where:).md)
- [func tryContains(where: (Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](just/trycontains(where:).md)
- [func allSatisfy((Output) -> Bool) -> Just<Bool>](just/allsatisfy(_:).md)
- [func tryAllSatisfy((Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](just/tryallsatisfy(_:).md)
### Applying Sequence Operations to Elements
- [func drop<P>(untilOutputFrom: P) -> Publishers.DropUntilOutput<Self, P>](just/drop(untiloutputfrom:).md)
  Ignores elements from the upstream publisher until it receives an element from a second publisher.
- [func dropFirst(Int) -> Optional<Output>.Publisher](just/dropfirst(_:).md)
- [func drop(while: (Output) -> Bool) -> Optional<Output>.Publisher](just/drop(while:).md)
- [func tryDrop(while: (Self.Output) throws -> Bool) -> Publishers.TryDropWhile<Self>](just/trydrop(while:).md)
  Omits elements from the upstream publisher until an error-throwing closure returns false, before republishing all remaining elements.
- [func append(Output...) -> Publishers.Sequence<[Output], Just<Output>.Failure>](just/append(_:)-7eyqj.md)
- [func append<S>(S) -> Publishers.Sequence<[Output], Just<Output>.Failure>](just/append(_:)-7sxlu.md)
- [func prepend<S>(S) -> Publishers.Sequence<[Output], Just<Output>.Failure>](just/prepend(_:)-39e57.md)
- [func prepend(Output...) -> Publishers.Sequence<[Output], Just<Output>.Failure>](just/prepend(_:)-7fg73.md)
- [func prefix(Int) -> Optional<Output>.Publisher](just/prefix(_:).md)
- [func prefix(while: (Output) -> Bool) -> Optional<Output>.Publisher](just/prefix(while:).md)
- [func tryPrefix(while: (Self.Output) throws -> Bool) -> Publishers.TryPrefixWhile<Self>](just/tryprefix(while:).md)
  Republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [func prefix<P>(untilOutputFrom: P) -> Publishers.PrefixUntilOutput<Self, P>](just/prefix(untiloutputfrom:).md)
  Republishes elements until another publisher emits an element.
### Selecting Specific Elements
- [func first() -> Just<Output>](just/first.md)
- [func first(where: (Output) -> Bool) -> Optional<Output>.Publisher](just/first(where:).md)
- [func tryFirst(where: (Self.Output) throws -> Bool) -> Publishers.TryFirstWhere<Self>](just/tryfirst(where:).md)
  Publishes the first element of a stream to satisfy a throwing predicate closure, then finishes normally.
- [func last() -> Just<Output>](just/last.md)
- [func last(where: (Output) -> Bool) -> Optional<Output>.Publisher](just/last(where:).md)
- [func tryLast(where: (Self.Output) throws -> Bool) -> Publishers.TryLastWhere<Self>](just/trylast(where:).md)
  Publishes the last element of a stream that satisfies an error-throwing predicate closure, after the stream finishes.
- [func output(at: Int) -> Optional<Output>.Publisher](just/output(at:).md)
- [func output<R>(in: R) -> Optional<Output>.Publisher](just/output(in:).md)
### Collecting and Republishing the Latest Elements from Multiple Publishers
- [func combineLatest<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.CombineLatest<Self, P>, T>](just/combinelatest(_:_:)-20das.md)
  Subscribes to an additional publisher and invokes a closure upon receiving output from either publisher.
- [func combineLatest<P>(P) -> Publishers.CombineLatest<Self, P>](just/combinelatest(_:).md)
  Subscribes to an additional publisher and publishes a tuple upon receiving output from either publisher.
- [func combineLatest<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.CombineLatest3<Self, P, Q>, T>](just/combinelatest(_:_:_:)-6gki5.md)
  Subscribes to two additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func combineLatest<P, Q>(P, Q) -> Publishers.CombineLatest3<Self, P, Q>](just/combinelatest(_:_:)-12egx.md)
  Subscribes to two additional publishers and publishes a tuple upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R, T>(P, Q, R, (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.CombineLatest4<Self, P, Q, R>, T>](just/combinelatest(_:_:_:_:).md)
  Subscribes to three additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R>(P, Q, R) -> Publishers.CombineLatest4<Self, P, Q, R>](just/combinelatest(_:_:_:)-79blm.md)
  Subscribes to three additional publishers and publishes a tuple upon receiving output from any of the publishers.
### Republishing Elements from Multiple Publishers as an Interleaved Stream
- [func merge<B, C>(with: B, C) -> Publishers.Merge3<Self, B, C>](just/merge(with:_:).md)
  Combines elements from this publisher with those from two other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D>(with: B, C, D) -> Publishers.Merge4<Self, B, C, D>](just/merge(with:_:_:).md)
  Combines elements from this publisher with those from three other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E>(with: B, C, D, E) -> Publishers.Merge5<Self, B, C, D, E>](just/merge(with:_:_:_:).md)
  Combines elements from this publisher with those from four other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F>(with: B, C, D, E, F) -> Publishers.Merge6<Self, B, C, D, E, F>](just/merge(with:_:_:_:_:).md)
  Combines elements from this publisher with those from five other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F, G>(with: B, C, D, E, F, G) -> Publishers.Merge7<Self, B, C, D, E, F, G>](just/merge(with:_:_:_:_:_:).md)
  Combines elements from this publisher with those from six other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F, G, H>(with: B, C, D, E, F, G, H) -> Publishers.Merge8<Self, B, C, D, E, F, G, H>](just/merge(with:_:_:_:_:_:_:).md)
  Combines elements from this publisher with those from seven other publishers, delivering an interleaved sequence of elements.
### Collecting and Republishing the Oldest Unconsumed Elements from Multiple Publishers
- [func zip<P>(P) -> Publishers.Zip<Self, P>](just/zip(_:).md)
  Combines elements from another publisher and deliver pairs of elements as tuples.
- [func zip<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.Zip<Self, P>, T>](just/zip(_:_:)-4z882.md)
  Combines elements from another publisher and delivers a transformed output.
- [func zip<P, Q>(P, Q) -> Publishers.Zip3<Self, P, Q>](just/zip(_:_:)-mjul.md)
  Combines elements from two other publishers and delivers groups of elements as tuples.
- [func zip<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.Zip3<Self, P, Q>, T>](just/zip(_:_:_:)-41m0z.md)
  Combines elements from two other publishers and delivers a transformed output.
- [func zip<P, Q, R>(P, Q, R) -> Publishers.Zip4<Self, P, Q, R>](just/zip(_:_:_:)-9fcfd.md)
  Combines elements from three other publishers and delivers groups of elements as tuples.
- [func zip<P, Q, R, T>(P, Q, R, (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.Zip4<Self, P, Q, R>, T>](just/zip(_:_:_:_:).md)
  Combines elements from three other publishers and delivers a transformed output.
### Republishing Elements by Subscribing to New Publishers
- [func flatMap<T, P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](just/flatmap(maxpublishers:_:)-6h2sh.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Publishers.SetFailureType<Self, P.Failure>>](just/flatmap(maxpublishers:_:)-99rva.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](just/flatmap(maxpublishers:_:)-7kd93.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<Publishers.SetFailureType<P, Self.Failure>, Self>](just/flatmap(maxpublishers:_:)-z2r1.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func switchToLatest() -> Publishers.SwitchToLatest<Self.Output, Publishers.SetFailureType<Self, Self.Output.Failure>>](just/switchtolatest.md)
  Republishes elements sent by the most recently received publisher.
### Handling Errors
- [func assertNoFailure(String, file: StaticString, line: UInt) -> Publishers.AssertNoFailure<Self>](just/assertnofailure(_:file:line:).md)
  Raises a fatal error when its upstream publisher fails, and otherwise republishes all received input.
- [func `catch`<P>((Self.Failure) -> P) -> Publishers.Catch<Self, P>](just/catch(_:).md)
  Handles errors from an upstream publisher by replacing it with another publisher.
- [func tryCatch<P>((Self.Failure) throws -> P) -> Publishers.TryCatch<Self, P>](just/trycatch(_:).md)
  Handles errors from an upstream publisher by either replacing it with another publisher or throwing a new error.
- [func retry(Int) -> Just<Output>](just/retry(_:).md)
### Controlling Timing
- [func measureInterval<S>(using: S, options: S.SchedulerOptions?) -> Publishers.MeasureInterval<Self, S>](just/measureinterval(using:options:).md)
  Measures and emits the time interval between events received from an upstream publisher.
- [func debounce<S>(for: S.SchedulerTimeType.Stride, scheduler: S, options: S.SchedulerOptions?) -> Publishers.Debounce<Self, S>](just/debounce(for:scheduler:options:).md)
  Publishes elements only after a specified time interval elapses between events.
- [func delay<S>(for: S.SchedulerTimeType.Stride, tolerance: S.SchedulerTimeType.Stride?, scheduler: S, options: S.SchedulerOptions?) -> Publishers.Delay<Self, S>](just/delay(for:tolerance:scheduler:options:).md)
  Delays delivery of all output to the downstream receiver by a specified amount of time on a particular scheduler.
- [func throttle<S>(for: S.SchedulerTimeType.Stride, scheduler: S, latest: Bool) -> Publishers.Throttle<Self, S>](just/throttle(for:scheduler:latest:).md)
  Publishes either the most-recent or first element published by the upstream publisher in the specified time interval.
- [func timeout<S>(S.SchedulerTimeType.Stride, scheduler: S, options: S.SchedulerOptions?, customError: (() -> Self.Failure)?) -> Publishers.Timeout<Self, S>](just/timeout(_:scheduler:options:customerror:).md)
  Terminates publishing if the upstream publisher exceeds the specified time interval without producing an element.
### Encoding and Decoding
- [func decode<Item, Coder>(type: Item.Type, decoder: Coder) -> Publishers.Decode<Self, Item, Coder>](just/decode(type:decoder:).md)
  Decodes the output from the upstream using a specified decoder.
- [func encode<Coder>(encoder: Coder) -> Publishers.Encode<Self, Coder>](just/encode(encoder:).md)
  Encodes the output from upstream using a specified encoder.
### Identifying Properties with Key Paths
- [func map<T>(KeyPath<Self.Output, T>) -> Publishers.MapKeyPath<Self, T>](just/map(_:)-7jaa0.md)
  Publishes the value of a key path.
- [func map<T0, T1>(KeyPath<Self.Output, T0>, KeyPath<Self.Output, T1>) -> Publishers.MapKeyPath2<Self, T0, T1>](just/map(_:_:).md)
  Publishes the values of two key paths as a tuple.
- [func map<T0, T1, T2>(KeyPath<Self.Output, T0>, KeyPath<Self.Output, T1>, KeyPath<Self.Output, T2>) -> Publishers.MapKeyPath3<Self, T0, T1, T2>](just/map(_:_:_:).md)
  Publishes the values of three key paths as a tuple.
### Working with Multiple Subscribers
- [func multicast<S>(() -> S) -> Publishers.Multicast<Self, S>](just/multicast(_:).md)
  Applies a closure to create a subject that delivers elements to subscribers.
- [func multicast<S>(subject: S) -> Publishers.Multicast<Self, S>](just/multicast(subject:).md)
  Provides a subject to deliver elements to multiple subscribers.
- [func share() -> Publishers.Share<Self>](just/share.md)
  Shares the output of an upstream publisher with multiple subscribers.
### Buffering Elements
- [func buffer(size: Int, prefetch: Publishers.PrefetchStrategy, whenFull: Publishers.BufferingStrategy<Self.Failure>) -> Publishers.Buffer<Self>](just/buffer(size:prefetch:whenfull:).md)
  Buffers elements received from an upstream publisher.
### Performing Type-Erasure
- [func eraseToAnyPublisher() -> AnyPublisher<Self.Output, Self.Failure>](just/erasetoanypublisher.md)
  Wraps this publisher with a type eraser.
### Specifying Schedulers
- [func subscribe<S>(on: S, options: S.SchedulerOptions?) -> Publishers.SubscribeOn<Self, S>](just/subscribe(on:options:).md)
  Specifies the scheduler on which to perform subscribe, cancel, and request operations.
- [func receive<S>(on: S, options: S.SchedulerOptions?) -> Publishers.ReceiveOn<Self, S>](just/receive(on:options:).md)
  Specifies the scheduler on which to receive elements from the publisher.
### Adding Explicit Connectability
- [func makeConnectable() -> Publishers.MakeConnectable<Self>](just/makeconnectable.md)
  Creates a connectable wrapper around the publisher.
### Connecting Simple Subscribers
- [func assign<Root>(to: ReferenceWritableKeyPath<Root, Self.Output>, on: Root) -> AnyCancellable](just/assign(to:on:).md)
  Assigns each element from a publisher to a property on an object.
- [func assign(to: inout Published<Self.Output>.Publisher)](just/assign(to:).md)
  Republishes elements received from a publisher, by assigning them to a property marked as a publisher.
- [func sink(receiveCompletion: (Subscribers.Completion<Self.Failure>) -> Void, receiveValue: (Self.Output) -> Void) -> AnyCancellable](just/sink(receivecompletion:receivevalue:).md)
  Attaches a subscriber with closure-based behavior.
- [func sink(receiveValue: (Self.Output) -> Void) -> AnyCancellable](just/sink(receivevalue:).md)
  Attaches a subscriber with closure-based behavior to a publisher that never fails.
### Debugging
- [func breakpoint(receiveSubscription: ((any Subscription) -> Bool)?, receiveOutput: ((Self.Output) -> Bool)?, receiveCompletion: ((Subscribers.Completion<Self.Failure>) -> Bool)?) -> Publishers.Breakpoint<Self>](just/breakpoint(receivesubscription:receiveoutput:receivecompletion:).md)
  Raises a debugger signal when a provided closure needs to stop the process in the debugger.
- [func breakpointOnError() -> Publishers.Breakpoint<Self>](just/breakpointonerror.md)
  Raises a debugger signal upon receiving a failure.
- [func handleEvents(receiveSubscription: ((any Subscription) -> Void)?, receiveOutput: ((Self.Output) -> Void)?, receiveCompletion: ((Subscribers.Completion<Self.Failure>) -> Void)?, receiveCancel: (() -> Void)?, receiveRequest: ((Subscribers.Demand) -> Void)?) -> Publishers.HandleEvents<Self>](just/handleevents(receivesubscription:receiveoutput:receivecompletion:receivecancel:receiverequest:).md)
  Performs the specified closures when publisher events occur.
- [func print(String, to: (any TextOutputStream)?) -> Publishers.Print<Self>](just/print(_:to:).md)
  Prints log messages for all publishing events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just-publisher-operators)*