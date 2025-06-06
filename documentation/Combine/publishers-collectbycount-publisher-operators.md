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
- [func receive<S>(subscriber: S)](publishers/collectbycount/receive(subscriber:).md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S)](publishers/collectbycount/subscribe(_:)-2oaa3.md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S) -> AnyCancellable](publishers/collectbycount/subscribe(_:)-6k3da.md)
  Attaches the specified subject to this publisher.
### Mapping Elements
- [func map<T>((Self.Output) -> T) -> Publishers.Map<Self, T>](publishers/collectbycount/map(_:)-4zo0y.md)
  Transforms all elements from the upstream publisher with a provided closure.
- [func tryMap<T>((Self.Output) throws -> T) -> Publishers.TryMap<Self, T>](publishers/collectbycount/trymap(_:).md)
  Transforms all elements from the upstream publisher with a provided error-throwing closure.
- [func mapError<E>((Self.Failure) -> E) -> Publishers.MapError<Self, E>](publishers/collectbycount/maperror(_:).md)
  Converts any failure from the upstream publisher into a new error.
- [func replaceNil<T>(with: T) -> Publishers.Map<Self, T>](publishers/collectbycount/replacenil(with:).md)
  Replaces nil elements in the stream with the provided element.
- [func scan<T>(T, (T, Self.Output) -> T) -> Publishers.Scan<Self, T>](publishers/collectbycount/scan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [func tryScan<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryScan<Self, T>](publishers/collectbycount/tryscan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to an error-throwing closure along with the last value returned by the closure.
- [func setFailureType<E>(to: E.Type) -> Publishers.SetFailureType<Self, E>](publishers/collectbycount/setfailuretype(to:).md)
  Changes the failure type declared by the upstream publisher.
### Filtering Elements
- [func filter((Self.Output) -> Bool) -> Publishers.Filter<Self>](publishers/collectbycount/filter(_:).md)
  Republishes all elements that match a provided closure.
- [func tryFilter((Self.Output) throws -> Bool) -> Publishers.TryFilter<Self>](publishers/collectbycount/tryfilter(_:).md)
  Republishes all elements that match a provided error-throwing closure.
- [func compactMap<T>((Self.Output) -> T?) -> Publishers.CompactMap<Self, T>](publishers/collectbycount/compactmap(_:).md)
  Calls a closure with each received element and publishes any returned optional that has a value.
- [func tryCompactMap<T>((Self.Output) throws -> T?) -> Publishers.TryCompactMap<Self, T>](publishers/collectbycount/trycompactmap(_:).md)
  Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [func removeDuplicates(by: (Self.Output, Self.Output) -> Bool) -> Publishers.RemoveDuplicates<Self>](publishers/collectbycount/removeduplicates(by:).md)
  Publishes only elements that don’t match the previous element, as evaluated by a provided closure.
- [func tryRemoveDuplicates(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryRemoveDuplicates<Self>](publishers/collectbycount/tryremoveduplicates(by:).md)
  Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [func replaceEmpty(with: Self.Output) -> Publishers.ReplaceEmpty<Self>](publishers/collectbycount/replaceempty(with:).md)
  Replaces an empty stream with the provided element.
- [func replaceError(with: Self.Output) -> Publishers.ReplaceError<Self>](publishers/collectbycount/replaceerror(with:).md)
  Replaces any errors in the stream with the provided element.
### Reducing Elements
- [func collect() -> Publishers.Collect<Self>](publishers/collectbycount/collect.md)
  Collects all received elements, and emits a single array of the collection when the upstream publisher finishes.
- [func collect(Int) -> Publishers.CollectByCount<Self>](publishers/collectbycount/collect(_:).md)
  Collects up to the specified number of elements, and then emits a single array of the collection.
- [func collect<S>(Publishers.TimeGroupingStrategy<S>, options: S.SchedulerOptions?) -> Publishers.CollectByTime<Self, S>](publishers/collectbycount/collect(_:options:).md)
  Collects elements by a given time-grouping strategy, and emits a single array of the collection.
- [func ignoreOutput() -> Publishers.IgnoreOutput<Self>](publishers/collectbycount/ignoreoutput.md)
  Ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [func reduce<T>(T, (T, Self.Output) -> T) -> Publishers.Reduce<Self, T>](publishers/collectbycount/reduce(_:_:).md)
  Applies a closure that collects each element of a stream and publishes a final result upon completion.
- [func tryReduce<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryReduce<Self, T>](publishers/collectbycount/tryreduce(_:_:).md)
  Applies an error-throwing closure that collects each element of a stream and publishes a final result upon completion.
### Applying Mathematical Operations on Elements
- [func count() -> Publishers.Count<Self>](publishers/collectbycount/count.md)
  Publishes the number of elements received from the upstream publisher.
- [func max(by: (Self.Output, Self.Output) -> Bool) -> Publishers.Comparison<Self>](publishers/collectbycount/max(by:).md)
  Publishes the maximum value received from the upstream publisher, using the provided ordering closure.
- [func tryMax(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](publishers/collectbycount/trymax(by:).md)
  Publishes the maximum value received from the upstream publisher, using the provided error-throwing closure to order the items.
- [func min(by: (Self.Output, Self.Output) -> Bool) -> Publishers.Comparison<Self>](publishers/collectbycount/min(by:).md)
  Publishes the minimum value received from the upstream publisher, after it finishes.
- [func tryMin(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](publishers/collectbycount/trymin(by:).md)
  Publishes the minimum value received from the upstream publisher, using the provided error-throwing closure to order the items.
### Applying Matching Criteria to Elements
- [func contains(where: (Self.Output) -> Bool) -> Publishers.ContainsWhere<Self>](publishers/collectbycount/contains(where:).md)
  Publishes a Boolean value upon receiving an element that satisfies the predicate closure.
- [func tryContains(where: (Self.Output) throws -> Bool) -> Publishers.TryContainsWhere<Self>](publishers/collectbycount/trycontains(where:).md)
  Publishes a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [func allSatisfy((Self.Output) -> Bool) -> Publishers.AllSatisfy<Self>](publishers/collectbycount/allsatisfy(_:).md)
  Publishes a single Boolean value that indicates whether all received elements pass a given predicate.
- [func tryAllSatisfy((Self.Output) throws -> Bool) -> Publishers.TryAllSatisfy<Self>](publishers/collectbycount/tryallsatisfy(_:).md)
  Publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.
### Applying Sequence Operations to Elements
- [func drop<P>(untilOutputFrom: P) -> Publishers.DropUntilOutput<Self, P>](publishers/collectbycount/drop(untiloutputfrom:).md)
  Ignores elements from the upstream publisher until it receives an element from a second publisher.
- [func dropFirst(Int) -> Publishers.Drop<Self>](publishers/collectbycount/dropfirst(_:).md)
  Omits the specified number of elements before republishing subsequent elements.
- [func drop(while: (Self.Output) -> Bool) -> Publishers.DropWhile<Self>](publishers/collectbycount/drop(while:).md)
  Omits elements from the upstream publisher until a given closure returns false, before republishing all remaining elements.
- [func tryDrop(while: (Self.Output) throws -> Bool) -> Publishers.TryDropWhile<Self>](publishers/collectbycount/trydrop(while:).md)
  Omits elements from the upstream publisher until an error-throwing closure returns false, before republishing all remaining elements.
- [func append(Self.Output...) -> Publishers.Concatenate<Self, Publishers.Sequence<[Self.Output], Self.Failure>>](publishers/collectbycount/append(_:).md)
  Appends a publisher’s output with the specified elements.
- [func prepend(Self.Output...) -> Publishers.Concatenate<Publishers.Sequence<[Self.Output], Self.Failure>, Self>](publishers/collectbycount/prepend(_:).md)
  Prefixes a publisher’s output with the specified values.
- [func prefix(Int) -> Publishers.Output<Self>](publishers/collectbycount/prefix(_:).md)
  Republishes elements up to the specified maximum count.
- [func prefix(while: (Self.Output) -> Bool) -> Publishers.PrefixWhile<Self>](publishers/collectbycount/prefix(while:).md)
  Republishes elements while a predicate closure indicates publishing should continue.
- [func tryPrefix(while: (Self.Output) throws -> Bool) -> Publishers.TryPrefixWhile<Self>](publishers/collectbycount/tryprefix(while:).md)
  Republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [func prefix<P>(untilOutputFrom: P) -> Publishers.PrefixUntilOutput<Self, P>](publishers/collectbycount/prefix(untiloutputfrom:).md)
  Republishes elements until another publisher emits an element.
### Selecting Specific Elements
- [func first() -> Publishers.First<Self>](publishers/collectbycount/first.md)
  Publishes the first element of a stream, then finishes.
- [func first(where: (Self.Output) -> Bool) -> Publishers.FirstWhere<Self>](publishers/collectbycount/first(where:).md)
  Publishes the first element of a stream to satisfy a predicate closure, then finishes normally.
- [func tryFirst(where: (Self.Output) throws -> Bool) -> Publishers.TryFirstWhere<Self>](publishers/collectbycount/tryfirst(where:).md)
  Publishes the first element of a stream to satisfy a throwing predicate closure, then finishes normally.
- [func last() -> Publishers.Last<Self>](publishers/collectbycount/last.md)
  Publishes the last element of a stream, after the stream finishes.
- [func last(where: (Self.Output) -> Bool) -> Publishers.LastWhere<Self>](publishers/collectbycount/last(where:).md)
  Publishes the last element of a stream that satisfies a predicate closure, after upstream finishes.
- [func tryLast(where: (Self.Output) throws -> Bool) -> Publishers.TryLastWhere<Self>](publishers/collectbycount/trylast(where:).md)
  Publishes the last element of a stream that satisfies an error-throwing predicate closure, after the stream finishes.
- [func output(at: Int) -> Publishers.Output<Self>](publishers/collectbycount/output(at:).md)
  Publishes a specific element, indicated by its index in the sequence of published elements.
- [func output<R>(in: R) -> Publishers.Output<Self>](publishers/collectbycount/output(in:).md)
  Publishes elements specified by their range in the sequence of published elements.
### Collecting and Republishing the Latest Elements from Multiple Publishers
- [func combineLatest<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.CombineLatest<Self, P>, T>](publishers/collectbycount/combinelatest(_:_:)-1yc00.md)
  Subscribes to an additional publisher and invokes a closure upon receiving output from either publisher.
- [func combineLatest<P>(P) -> Publishers.CombineLatest<Self, P>](publishers/collectbycount/combinelatest(_:).md)
  Subscribes to an additional publisher and publishes a tuple upon receiving output from either publisher.
- [func combineLatest<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.CombineLatest3<Self, P, Q>, T>](publishers/collectbycount/combinelatest(_:_:_:)-678ha.md)
  Subscribes to two additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func combineLatest<P, Q>(P, Q) -> Publishers.CombineLatest3<Self, P, Q>](publishers/collectbycount/combinelatest(_:_:)-4eocg.md)
  Subscribes to two additional publishers and publishes a tuple upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R, T>(P, Q, R, (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.CombineLatest4<Self, P, Q, R>, T>](publishers/collectbycount/combinelatest(_:_:_:_:).md)
  Subscribes to three additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R>(P, Q, R) -> Publishers.CombineLatest4<Self, P, Q, R>](publishers/collectbycount/combinelatest(_:_:_:)-5rhce.md)
  Subscribes to three additional publishers and publishes a tuple upon receiving output from any of the publishers.
### Republishing Elements from Multiple Publishers as an Interleaved Stream
- [func merge(with: Self) -> Publishers.MergeMany<Self>](publishers/collectbycount/merge(with:).md)
  Combines elements from this publisher with those from another publisher of the same type, delivering an interleaved sequence of elements.
- [func merge<B, C>(with: B, C) -> Publishers.Merge3<Self, B, C>](publishers/collectbycount/merge(with:_:).md)
  Combines elements from this publisher with those from two other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D>(with: B, C, D) -> Publishers.Merge4<Self, B, C, D>](publishers/collectbycount/merge(with:_:_:).md)
  Combines elements from this publisher with those from three other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E>(with: B, C, D, E) -> Publishers.Merge5<Self, B, C, D, E>](publishers/collectbycount/merge(with:_:_:_:).md)
  Combines elements from this publisher with those from four other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F>(with: B, C, D, E, F) -> Publishers.Merge6<Self, B, C, D, E, F>](publishers/collectbycount/merge(with:_:_:_:_:).md)
  Combines elements from this publisher with those from five other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F, G>(with: B, C, D, E, F, G) -> Publishers.Merge7<Self, B, C, D, E, F, G>](publishers/collectbycount/merge(with:_:_:_:_:_:).md)
  Combines elements from this publisher with those from six other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F, G, H>(with: B, C, D, E, F, G, H) -> Publishers.Merge8<Self, B, C, D, E, F, G, H>](publishers/collectbycount/merge(with:_:_:_:_:_:_:).md)
  Combines elements from this publisher with those from seven other publishers, delivering an interleaved sequence of elements.
### Collecting and Republishing the Oldest Unconsumed Elements from Multiple Publishers
- [func zip<P>(P) -> Publishers.Zip<Self, P>](publishers/collectbycount/zip(_:).md)
  Combines elements from another publisher and deliver pairs of elements as tuples.
- [func zip<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.Zip<Self, P>, T>](publishers/collectbycount/zip(_:_:)-7n4y6.md)
  Combines elements from another publisher and delivers a transformed output.
- [func zip<P, Q>(P, Q) -> Publishers.Zip3<Self, P, Q>](publishers/collectbycount/zip(_:_:)-3sa73.md)
  Combines elements from two other publishers and delivers groups of elements as tuples.
- [func zip<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.Zip3<Self, P, Q>, T>](publishers/collectbycount/zip(_:_:_:)-9bt0c.md)
  Combines elements from two other publishers and delivers a transformed output.
- [func zip<P, Q, R>(P, Q, R) -> Publishers.Zip4<Self, P, Q, R>](publishers/collectbycount/zip(_:_:_:)-7cwbn.md)
  Combines elements from three other publishers and delivers groups of elements as tuples.
- [func zip<P, Q, R, T>(P, Q, R, (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.Zip4<Self, P, Q, R>, T>](publishers/collectbycount/zip(_:_:_:_:).md)
  Combines elements from three other publishers and delivers a transformed output.
### Republishing Elements by Subscribing to New Publishers
- [func flatMap<T, P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](publishers/collectbycount/flatmap(maxpublishers:_:)-7jkb7.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Publishers.SetFailureType<Self, P.Failure>>](publishers/collectbycount/flatmap(maxpublishers:_:)-3c6r8.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](publishers/collectbycount/flatmap(maxpublishers:_:)-79ro3.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<Publishers.SetFailureType<P, Self.Failure>, Self>](publishers/collectbycount/flatmap(maxpublishers:_:)-6nufx.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
### Handling Errors
- [func assertNoFailure(String, file: StaticString, line: UInt) -> Publishers.AssertNoFailure<Self>](publishers/collectbycount/assertnofailure(_:file:line:).md)
  Raises a fatal error when its upstream publisher fails, and otherwise republishes all received input.
- [func `catch`<P>((Self.Failure) -> P) -> Publishers.Catch<Self, P>](publishers/collectbycount/catch(_:).md)
  Handles errors from an upstream publisher by replacing it with another publisher.
- [func tryCatch<P>((Self.Failure) throws -> P) -> Publishers.TryCatch<Self, P>](publishers/collectbycount/trycatch(_:).md)
  Handles errors from an upstream publisher by either replacing it with another publisher or throwing a new error.
- [func retry(Int) -> Publishers.Retry<Self>](publishers/collectbycount/retry(_:).md)
  Attempts to recreate a failed subscription with the upstream publisher up to the number of times you specify.
### Controlling Timing
- [func measureInterval<S>(using: S, options: S.SchedulerOptions?) -> Publishers.MeasureInterval<Self, S>](publishers/collectbycount/measureinterval(using:options:).md)
  Measures and emits the time interval between events received from an upstream publisher.
- [func debounce<S>(for: S.SchedulerTimeType.Stride, scheduler: S, options: S.SchedulerOptions?) -> Publishers.Debounce<Self, S>](publishers/collectbycount/debounce(for:scheduler:options:).md)
  Publishes elements only after a specified time interval elapses between events.
- [func delay<S>(for: S.SchedulerTimeType.Stride, tolerance: S.SchedulerTimeType.Stride?, scheduler: S, options: S.SchedulerOptions?) -> Publishers.Delay<Self, S>](publishers/collectbycount/delay(for:tolerance:scheduler:options:).md)
  Delays delivery of all output to the downstream receiver by a specified amount of time on a particular scheduler.
- [func throttle<S>(for: S.SchedulerTimeType.Stride, scheduler: S, latest: Bool) -> Publishers.Throttle<Self, S>](publishers/collectbycount/throttle(for:scheduler:latest:).md)
  Publishes either the most-recent or first element published by the upstream publisher in the specified time interval.
- [func timeout<S>(S.SchedulerTimeType.Stride, scheduler: S, options: S.SchedulerOptions?, customError: (() -> Self.Failure)?) -> Publishers.Timeout<Self, S>](publishers/collectbycount/timeout(_:scheduler:options:customerror:).md)
  Terminates publishing if the upstream publisher exceeds the specified time interval without producing an element.
### Encoding and Decoding
- [func decode<Item, Coder>(type: Item.Type, decoder: Coder) -> Publishers.Decode<Self, Item, Coder>](publishers/collectbycount/decode(type:decoder:).md)
  Decodes the output from the upstream using a specified decoder.
### Identifying Properties with Key Paths
- [func map<T>(KeyPath<Self.Output, T>) -> Publishers.MapKeyPath<Self, T>](publishers/collectbycount/map(_:)-u4q3.md)
  Publishes the value of a key path.
- [func map<T0, T1>(KeyPath<Self.Output, T0>, KeyPath<Self.Output, T1>) -> Publishers.MapKeyPath2<Self, T0, T1>](publishers/collectbycount/map(_:_:).md)
  Publishes the values of two key paths as a tuple.
- [func map<T0, T1, T2>(KeyPath<Self.Output, T0>, KeyPath<Self.Output, T1>, KeyPath<Self.Output, T2>) -> Publishers.MapKeyPath3<Self, T0, T1, T2>](publishers/collectbycount/map(_:_:_:).md)
  Publishes the values of three key paths as a tuple.
### Working with Multiple Subscribers
- [func multicast<S>(() -> S) -> Publishers.Multicast<Self, S>](publishers/collectbycount/multicast(_:).md)
  Applies a closure to create a subject that delivers elements to subscribers.
- [func multicast<S>(subject: S) -> Publishers.Multicast<Self, S>](publishers/collectbycount/multicast(subject:).md)
  Provides a subject to deliver elements to multiple subscribers.
- [func share() -> Publishers.Share<Self>](publishers/collectbycount/share.md)
  Shares the output of an upstream publisher with multiple subscribers.
### Buffering Elements
- [func buffer(size: Int, prefetch: Publishers.PrefetchStrategy, whenFull: Publishers.BufferingStrategy<Self.Failure>) -> Publishers.Buffer<Self>](publishers/collectbycount/buffer(size:prefetch:whenfull:).md)
  Buffers elements received from an upstream publisher.
### Performing Type-Erasure
- [func eraseToAnyPublisher() -> AnyPublisher<Self.Output, Self.Failure>](publishers/collectbycount/erasetoanypublisher.md)
  Wraps this publisher with a type eraser.
### Specifying Schedulers
- [func subscribe<S>(on: S, options: S.SchedulerOptions?) -> Publishers.SubscribeOn<Self, S>](publishers/collectbycount/subscribe(on:options:).md)
  Specifies the scheduler on which to perform subscribe, cancel, and request operations.
- [func receive<S>(on: S, options: S.SchedulerOptions?) -> Publishers.ReceiveOn<Self, S>](publishers/collectbycount/receive(on:options:).md)
  Specifies the scheduler on which to receive elements from the publisher.
### Adding Explicit Connectability
- [func makeConnectable() -> Publishers.MakeConnectable<Self>](publishers/collectbycount/makeconnectable.md)
  Creates a connectable wrapper around the publisher.
### Connecting Simple Subscribers
- [func assign<Root>(to: ReferenceWritableKeyPath<Root, Self.Output>, on: Root) -> AnyCancellable](publishers/collectbycount/assign(to:on:).md)
  Assigns each element from a publisher to a property on an object.
- [func assign(to: inout Published<Self.Output>.Publisher)](publishers/collectbycount/assign(to:).md)
  Republishes elements received from a publisher, by assigning them to a property marked as a publisher.
- [func sink(receiveCompletion: (Subscribers.Completion<Self.Failure>) -> Void, receiveValue: (Self.Output) -> Void) -> AnyCancellable](publishers/collectbycount/sink(receivecompletion:receivevalue:).md)
  Attaches a subscriber with closure-based behavior.
- [func sink(receiveValue: (Self.Output) -> Void) -> AnyCancellable](publishers/collectbycount/sink(receivevalue:).md)
  Attaches a subscriber with closure-based behavior to a publisher that never fails.
### Debugging
- [func breakpoint(receiveSubscription: ((any Subscription) -> Bool)?, receiveOutput: ((Self.Output) -> Bool)?, receiveCompletion: ((Subscribers.Completion<Self.Failure>) -> Bool)?) -> Publishers.Breakpoint<Self>](publishers/collectbycount/breakpoint(receivesubscription:receiveoutput:receivecompletion:).md)
  Raises a debugger signal when a provided closure needs to stop the process in the debugger.
- [func breakpointOnError() -> Publishers.Breakpoint<Self>](publishers/collectbycount/breakpointonerror.md)
  Raises a debugger signal upon receiving a failure.
- [func handleEvents(receiveSubscription: ((any Subscription) -> Void)?, receiveOutput: ((Self.Output) -> Void)?, receiveCompletion: ((Subscribers.Completion<Self.Failure>) -> Void)?, receiveCancel: (() -> Void)?, receiveRequest: ((Subscribers.Demand) -> Void)?) -> Publishers.HandleEvents<Self>](publishers/collectbycount/handleevents(receivesubscription:receiveoutput:receivecompletion:receivecancel:receiverequest:).md)
  Performs the specified closures when publisher events occur.
- [func print(String, to: (any TextOutputStream)?) -> Publishers.Print<Self>](publishers/collectbycount/print(_:to:).md)
  Prints log messages for all publishing events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers-collectbycount-publisher-operators)*