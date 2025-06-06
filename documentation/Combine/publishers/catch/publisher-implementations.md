# Publisher Implementations

**Framework**: Combine

## Topics

### Instance Properties
- [var values: AsyncPublisher<Self>](publishers/catch/values-33vb.md)
  The elements produced by the publisher, as an asynchronous sequence.
- [var values: AsyncThrowingPublisher<Self>](publishers/catch/values-8vg1w.md)
  The elements produced by the publisher, as a throwing asynchronous sequence.
### Instance Methods
- [func allSatisfy((Self.Output) -> Bool) -> Publishers.AllSatisfy<Self>](publishers/catch/allsatisfy(_:).md)
  Publishes a single Boolean value that indicates whether all received elements pass a given predicate.
- [func append(Self.Output...) -> Publishers.Concatenate<Self, Publishers.Sequence<[Self.Output], Self.Failure>>](publishers/catch/append(_:).md)
  Appends a publisher’s output with the specified elements.
- [func assertNoFailure(String, file: StaticString, line: UInt) -> Publishers.AssertNoFailure<Self>](publishers/catch/assertnofailure(_:file:line:).md)
  Raises a fatal error when its upstream publisher fails, and otherwise republishes all received input.
- [func assign(to: inout Published<Self.Output>.Publisher)](publishers/catch/assign(to:).md)
  Republishes elements received from a publisher, by assigning them to a property marked as a publisher.
- [func assign<Root>(to: ReferenceWritableKeyPath<Root, Self.Output>, on: Root) -> AnyCancellable](publishers/catch/assign(to:on:).md)
  Assigns each element from a publisher to a property on an object.
- [func breakpoint(receiveSubscription: ((any Subscription) -> Bool)?, receiveOutput: ((Self.Output) -> Bool)?, receiveCompletion: ((Subscribers.Completion<Self.Failure>) -> Bool)?) -> Publishers.Breakpoint<Self>](publishers/catch/breakpoint(receivesubscription:receiveoutput:receivecompletion:).md)
  Raises a debugger signal when a provided closure needs to stop the process in the debugger.
- [func breakpointOnError() -> Publishers.Breakpoint<Self>](publishers/catch/breakpointonerror.md)
  Raises a debugger signal upon receiving a failure.
- [func buffer(size: Int, prefetch: Publishers.PrefetchStrategy, whenFull: Publishers.BufferingStrategy<Self.Failure>) -> Publishers.Buffer<Self>](publishers/catch/buffer(size:prefetch:whenfull:).md)
  Buffers elements received from an upstream publisher.
- [func `catch`<P>((Self.Failure) -> P) -> Publishers.Catch<Self, P>](publishers/catch/catch(_:).md)
  Handles errors from an upstream publisher by replacing it with another publisher.
- [func collect() -> Publishers.Collect<Self>](publishers/catch/collect.md)
  Collects all received elements, and emits a single array of the collection when the upstream publisher finishes.
- [func collect(Int) -> Publishers.CollectByCount<Self>](publishers/catch/collect(_:).md)
  Collects up to the specified number of elements, and then emits a single array of the collection.
- [func collect<S>(Publishers.TimeGroupingStrategy<S>, options: S.SchedulerOptions?) -> Publishers.CollectByTime<Self, S>](publishers/catch/collect(_:options:).md)
  Collects elements by a given time-grouping strategy, and emits a single array of the collection.
- [func combineLatest<P>(P) -> Publishers.CombineLatest<Self, P>](publishers/catch/combinelatest(_:).md)
  Subscribes to an additional publisher and publishes a tuple upon receiving output from either publisher.
- [func combineLatest<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.CombineLatest<Self, P>, T>](publishers/catch/combinelatest(_:_:)-2s61.md)
  Subscribes to an additional publisher and invokes a closure upon receiving output from either publisher.
- [func combineLatest<P, Q>(P, Q) -> Publishers.CombineLatest3<Self, P, Q>](publishers/catch/combinelatest(_:_:)-9mnf1.md)
  Subscribes to two additional publishers and publishes a tuple upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R>(P, Q, R) -> Publishers.CombineLatest4<Self, P, Q, R>](publishers/catch/combinelatest(_:_:_:)-8yhsf.md)
  Subscribes to three additional publishers and publishes a tuple upon receiving output from any of the publishers.
- [func combineLatest<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.CombineLatest3<Self, P, Q>, T>](publishers/catch/combinelatest(_:_:_:)-94mq8.md)
  Subscribes to two additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R, T>(P, Q, R, (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.CombineLatest4<Self, P, Q, R>, T>](publishers/catch/combinelatest(_:_:_:_:).md)
  Subscribes to three additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func compactMap<T>((Self.Output) -> T?) -> Publishers.CompactMap<Self, T>](publishers/catch/compactmap(_:).md)
  Calls a closure with each received element and publishes any returned optional that has a value.
- [func contains(Self.Output) -> Publishers.Contains<Self>](publishers/catch/contains(_:).md)
  Publishes a Boolean value upon receiving an element equal to the argument.
- [func contains(where: (Self.Output) -> Bool) -> Publishers.ContainsWhere<Self>](publishers/catch/contains(where:).md)
  Publishes a Boolean value upon receiving an element that satisfies the predicate closure.
- [func count() -> Publishers.Count<Self>](publishers/catch/count.md)
  Publishes the number of elements received from the upstream publisher.
- [func debounce<S>(for: S.SchedulerTimeType.Stride, scheduler: S, options: S.SchedulerOptions?) -> Publishers.Debounce<Self, S>](publishers/catch/debounce(for:scheduler:options:).md)
  Publishes elements only after a specified time interval elapses between events.
- [func decode<Item, Coder>(type: Item.Type, decoder: Coder) -> Publishers.Decode<Self, Item, Coder>](publishers/catch/decode(type:decoder:).md)
  Decodes the output from the upstream using a specified decoder.
- [func delay<S>(for: S.SchedulerTimeType.Stride, tolerance: S.SchedulerTimeType.Stride?, scheduler: S, options: S.SchedulerOptions?) -> Publishers.Delay<Self, S>](publishers/catch/delay(for:tolerance:scheduler:options:).md)
  Delays delivery of all output to the downstream receiver by a specified amount of time on a particular scheduler.
- [func drop<P>(untilOutputFrom: P) -> Publishers.DropUntilOutput<Self, P>](publishers/catch/drop(untiloutputfrom:).md)
  Ignores elements from the upstream publisher until it receives an element from a second publisher.
- [func drop(while: (Self.Output) -> Bool) -> Publishers.DropWhile<Self>](publishers/catch/drop(while:).md)
  Omits elements from the upstream publisher until a given closure returns false, before republishing all remaining elements.
- [func dropFirst(Int) -> Publishers.Drop<Self>](publishers/catch/dropfirst(_:).md)
  Omits the specified number of elements before republishing subsequent elements.
- [func encode<Coder>(encoder: Coder) -> Publishers.Encode<Self, Coder>](publishers/catch/encode(encoder:).md)
  Encodes the output from upstream using a specified encoder.
- [func eraseToAnyPublisher() -> AnyPublisher<Self.Output, Self.Failure>](publishers/catch/erasetoanypublisher.md)
  Wraps this publisher with a type eraser.
- [func filter((Self.Output) -> Bool) -> Publishers.Filter<Self>](publishers/catch/filter(_:).md)
  Republishes all elements that match a provided closure.
- [func first() -> Publishers.First<Self>](publishers/catch/first.md)
  Publishes the first element of a stream, then finishes.
- [func first(where: (Self.Output) -> Bool) -> Publishers.FirstWhere<Self>](publishers/catch/first(where:).md)
  Publishes the first element of a stream to satisfy a predicate closure, then finishes normally.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](publishers/catch/flatmap(maxpublishers:_:)-1jsr0.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<Publishers.SetFailureType<P, Self.Failure>, Self>](publishers/catch/flatmap(maxpublishers:_:)-6fmzg.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Publishers.SetFailureType<Self, P.Failure>>](publishers/catch/flatmap(maxpublishers:_:)-9nqei.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<T, P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](publishers/catch/flatmap(maxpublishers:_:)-9nww4.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func handleEvents(receiveSubscription: ((any Subscription) -> Void)?, receiveOutput: ((Self.Output) -> Void)?, receiveCompletion: ((Subscribers.Completion<Self.Failure>) -> Void)?, receiveCancel: (() -> Void)?, receiveRequest: ((Subscribers.Demand) -> Void)?) -> Publishers.HandleEvents<Self>](publishers/catch/handleevents(receivesubscription:receiveoutput:receivecompletion:receivecancel:receiverequest:).md)
  Performs the specified closures when publisher events occur.
- [func ignoreOutput() -> Publishers.IgnoreOutput<Self>](publishers/catch/ignoreoutput.md)
  Ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [func last() -> Publishers.Last<Self>](publishers/catch/last.md)
  Publishes the last element of a stream, after the stream finishes.
- [func last(where: (Self.Output) -> Bool) -> Publishers.LastWhere<Self>](publishers/catch/last(where:).md)
  Publishes the last element of a stream that satisfies a predicate closure, after upstream finishes.
- [func makeConnectable() -> Publishers.MakeConnectable<Self>](publishers/catch/makeconnectable.md)
  Creates a connectable wrapper around the publisher.
- [func map<T>(KeyPath<Self.Output, T>) -> Publishers.MapKeyPath<Self, T>](publishers/catch/map(_:)-49jrw.md)
  Publishes the value of a key path.
- [func map<T>((Self.Output) -> T) -> Publishers.Map<Self, T>](publishers/catch/map(_:)-6vw93.md)
  Transforms all elements from the upstream publisher with a provided closure.
- [func map<T0, T1>(KeyPath<Self.Output, T0>, KeyPath<Self.Output, T1>) -> Publishers.MapKeyPath2<Self, T0, T1>](publishers/catch/map(_:_:).md)
  Publishes the values of two key paths as a tuple.
- [func map<T0, T1, T2>(KeyPath<Self.Output, T0>, KeyPath<Self.Output, T1>, KeyPath<Self.Output, T2>) -> Publishers.MapKeyPath3<Self, T0, T1, T2>](publishers/catch/map(_:_:_:).md)
  Publishes the values of three key paths as a tuple.
- [func mapError<E>((Self.Failure) -> E) -> Publishers.MapError<Self, E>](publishers/catch/maperror(_:).md)
  Converts any failure from the upstream publisher into a new error.
- [func max() -> Publishers.Comparison<Self>](publishers/catch/max.md)
  Publishes the maximum value received from the upstream publisher, after it finishes.
- [func max(by: (Self.Output, Self.Output) -> Bool) -> Publishers.Comparison<Self>](publishers/catch/max(by:).md)
  Publishes the maximum value received from the upstream publisher, using the provided ordering closure.
- [func measureInterval<S>(using: S, options: S.SchedulerOptions?) -> Publishers.MeasureInterval<Self, S>](publishers/catch/measureinterval(using:options:).md)
  Measures and emits the time interval between events received from an upstream publisher.
- [func merge(with: Self) -> Publishers.MergeMany<Self>](publishers/catch/merge(with:).md)
  Combines elements from this publisher with those from another publisher of the same type, delivering an interleaved sequence of elements.
- [func merge<B, C>(with: B, C) -> Publishers.Merge3<Self, B, C>](publishers/catch/merge(with:_:).md)
  Combines elements from this publisher with those from two other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D>(with: B, C, D) -> Publishers.Merge4<Self, B, C, D>](publishers/catch/merge(with:_:_:).md)
  Combines elements from this publisher with those from three other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E>(with: B, C, D, E) -> Publishers.Merge5<Self, B, C, D, E>](publishers/catch/merge(with:_:_:_:).md)
  Combines elements from this publisher with those from four other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F>(with: B, C, D, E, F) -> Publishers.Merge6<Self, B, C, D, E, F>](publishers/catch/merge(with:_:_:_:_:).md)
  Combines elements from this publisher with those from five other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F, G>(with: B, C, D, E, F, G) -> Publishers.Merge7<Self, B, C, D, E, F, G>](publishers/catch/merge(with:_:_:_:_:_:).md)
  Combines elements from this publisher with those from six other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F, G, H>(with: B, C, D, E, F, G, H) -> Publishers.Merge8<Self, B, C, D, E, F, G, H>](publishers/catch/merge(with:_:_:_:_:_:_:).md)
  Combines elements from this publisher with those from seven other publishers, delivering an interleaved sequence of elements.
- [func min() -> Publishers.Comparison<Self>](publishers/catch/min.md)
  Publishes the minimum value received from the upstream publisher, after it finishes.
- [func min(by: (Self.Output, Self.Output) -> Bool) -> Publishers.Comparison<Self>](publishers/catch/min(by:).md)
  Publishes the minimum value received from the upstream publisher, after it finishes.
- [func multicast<S>(() -> S) -> Publishers.Multicast<Self, S>](publishers/catch/multicast(_:).md)
  Applies a closure to create a subject that delivers elements to subscribers.
- [func multicast<S>(subject: S) -> Publishers.Multicast<Self, S>](publishers/catch/multicast(subject:).md)
  Provides a subject to deliver elements to multiple subscribers.
- [func output(at: Int) -> Publishers.Output<Self>](publishers/catch/output(at:).md)
  Publishes a specific element, indicated by its index in the sequence of published elements.
- [func output<R>(in: R) -> Publishers.Output<Self>](publishers/catch/output(in:).md)
  Publishes elements specified by their range in the sequence of published elements.
- [func prefix(Int) -> Publishers.Output<Self>](publishers/catch/prefix(_:).md)
  Republishes elements up to the specified maximum count.
- [func prefix<P>(untilOutputFrom: P) -> Publishers.PrefixUntilOutput<Self, P>](publishers/catch/prefix(untiloutputfrom:).md)
  Republishes elements until another publisher emits an element.
- [func prefix(while: (Self.Output) -> Bool) -> Publishers.PrefixWhile<Self>](publishers/catch/prefix(while:).md)
  Republishes elements while a predicate closure indicates publishing should continue.
- [func prepend(Self.Output...) -> Publishers.Concatenate<Publishers.Sequence<[Self.Output], Self.Failure>, Self>](publishers/catch/prepend(_:).md)
  Prefixes a publisher’s output with the specified values.
- [func print(String, to: (any TextOutputStream)?) -> Publishers.Print<Self>](publishers/catch/print(_:to:).md)
  Prints log messages for all publishing events.
- [func receive<S>(on: S, options: S.SchedulerOptions?) -> Publishers.ReceiveOn<Self, S>](publishers/catch/receive(on:options:).md)
  Specifies the scheduler on which to receive elements from the publisher.
- [func reduce<T>(T, (T, Self.Output) -> T) -> Publishers.Reduce<Self, T>](publishers/catch/reduce(_:_:).md)
  Applies a closure that collects each element of a stream and publishes a final result upon completion.
- [func removeDuplicates() -> Publishers.RemoveDuplicates<Self>](publishers/catch/removeduplicates.md)
  Publishes only elements that don’t match the previous element.
- [func removeDuplicates(by: (Self.Output, Self.Output) -> Bool) -> Publishers.RemoveDuplicates<Self>](publishers/catch/removeduplicates(by:).md)
  Publishes only elements that don’t match the previous element, as evaluated by a provided closure.
- [func replaceEmpty(with: Self.Output) -> Publishers.ReplaceEmpty<Self>](publishers/catch/replaceempty(with:).md)
  Replaces an empty stream with the provided element.
- [func replaceError(with: Self.Output) -> Publishers.ReplaceError<Self>](publishers/catch/replaceerror(with:).md)
  Replaces any errors in the stream with the provided element.
- [func replaceNil<T>(with: T) -> Publishers.Map<Self, T>](publishers/catch/replacenil(with:).md)
  Replaces nil elements in the stream with the provided element.
- [func retry(Int) -> Publishers.Retry<Self>](publishers/catch/retry(_:).md)
  Attempts to recreate a failed subscription with the upstream publisher up to the number of times you specify.
- [func scan<T>(T, (T, Self.Output) -> T) -> Publishers.Scan<Self, T>](publishers/catch/scan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [func setFailureType<E>(to: E.Type) -> Publishers.SetFailureType<Self, E>](publishers/catch/setfailuretype(to:).md)
  Changes the failure type declared by the upstream publisher.
- [func share() -> Publishers.Share<Self>](publishers/catch/share.md)
  Shares the output of an upstream publisher with multiple subscribers.
- [func sink(receiveCompletion: (Subscribers.Completion<Self.Failure>) -> Void, receiveValue: (Self.Output) -> Void) -> AnyCancellable](publishers/catch/sink(receivecompletion:receivevalue:).md)
  Attaches a subscriber with closure-based behavior.
- [func sink(receiveValue: (Self.Output) -> Void) -> AnyCancellable](publishers/catch/sink(receivevalue:).md)
  Attaches a subscriber with closure-based behavior to a publisher that never fails.
- [func subscribe<S>(S) -> AnyCancellable](publishers/catch/subscribe(_:)-4nr4e.md)
  Attaches the specified subject to this publisher.
- [func subscribe<S>(S)](publishers/catch/subscribe(_:)-690ry.md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(on: S, options: S.SchedulerOptions?) -> Publishers.SubscribeOn<Self, S>](publishers/catch/subscribe(on:options:).md)
  Specifies the scheduler on which to perform subscribe, cancel, and request operations.
- [func switchToLatest() -> Publishers.SwitchToLatest<Self.Output, Publishers.SetFailureType<Self, Self.Output.Failure>>](publishers/catch/switchtolatest.md)
  Republishes elements sent by the most recently received publisher.
- [func throttle<S>(for: S.SchedulerTimeType.Stride, scheduler: S, latest: Bool) -> Publishers.Throttle<Self, S>](publishers/catch/throttle(for:scheduler:latest:).md)
  Publishes either the most-recent or first element published by the upstream publisher in the specified time interval.
- [func timeout<S>(S.SchedulerTimeType.Stride, scheduler: S, options: S.SchedulerOptions?, customError: (() -> Self.Failure)?) -> Publishers.Timeout<Self, S>](publishers/catch/timeout(_:scheduler:options:customerror:).md)
  Terminates publishing if the upstream publisher exceeds the specified time interval without producing an element.
- [func tryAllSatisfy((Self.Output) throws -> Bool) -> Publishers.TryAllSatisfy<Self>](publishers/catch/tryallsatisfy(_:).md)
  Publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.
- [func tryCatch<P>((Self.Failure) throws -> P) -> Publishers.TryCatch<Self, P>](publishers/catch/trycatch(_:).md)
  Handles errors from an upstream publisher by either replacing it with another publisher or throwing a new error.
- [func tryCompactMap<T>((Self.Output) throws -> T?) -> Publishers.TryCompactMap<Self, T>](publishers/catch/trycompactmap(_:).md)
  Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [func tryContains(where: (Self.Output) throws -> Bool) -> Publishers.TryContainsWhere<Self>](publishers/catch/trycontains(where:).md)
  Publishes a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [func tryDrop(while: (Self.Output) throws -> Bool) -> Publishers.TryDropWhile<Self>](publishers/catch/trydrop(while:).md)
  Omits elements from the upstream publisher until an error-throwing closure returns false, before republishing all remaining elements.
- [func tryFilter((Self.Output) throws -> Bool) -> Publishers.TryFilter<Self>](publishers/catch/tryfilter(_:).md)
  Republishes all elements that match a provided error-throwing closure.
- [func tryFirst(where: (Self.Output) throws -> Bool) -> Publishers.TryFirstWhere<Self>](publishers/catch/tryfirst(where:).md)
  Publishes the first element of a stream to satisfy a throwing predicate closure, then finishes normally.
- [func tryLast(where: (Self.Output) throws -> Bool) -> Publishers.TryLastWhere<Self>](publishers/catch/trylast(where:).md)
  Publishes the last element of a stream that satisfies an error-throwing predicate closure, after the stream finishes.
- [func tryMap<T>((Self.Output) throws -> T) -> Publishers.TryMap<Self, T>](publishers/catch/trymap(_:).md)
  Transforms all elements from the upstream publisher with a provided error-throwing closure.
- [func tryMax(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](publishers/catch/trymax(by:).md)
  Publishes the maximum value received from the upstream publisher, using the provided error-throwing closure to order the items.
- [func tryMin(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](publishers/catch/trymin(by:).md)
  Publishes the minimum value received from the upstream publisher, using the provided error-throwing closure to order the items.
- [func tryPrefix(while: (Self.Output) throws -> Bool) -> Publishers.TryPrefixWhile<Self>](publishers/catch/tryprefix(while:).md)
  Republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [func tryReduce<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryReduce<Self, T>](publishers/catch/tryreduce(_:_:).md)
  Applies an error-throwing closure that collects each element of a stream and publishes a final result upon completion.
- [func tryRemoveDuplicates(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryRemoveDuplicates<Self>](publishers/catch/tryremoveduplicates(by:).md)
  Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [func tryScan<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryScan<Self, T>](publishers/catch/tryscan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to an error-throwing closure along with the last value returned by the closure.
- [func zip<P>(P) -> Publishers.Zip<Self, P>](publishers/catch/zip(_:).md)
  Combines elements from another publisher and deliver pairs of elements as tuples.
- [func zip<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.Zip<Self, P>, T>](publishers/catch/zip(_:_:)-3e1l1.md)
  Combines elements from another publisher and delivers a transformed output.
- [func zip<P, Q>(P, Q) -> Publishers.Zip3<Self, P, Q>](publishers/catch/zip(_:_:)-3kejn.md)
  Combines elements from two other publishers and delivers groups of elements as tuples.
- [func zip<P, Q, R>(P, Q, R) -> Publishers.Zip4<Self, P, Q, R>](publishers/catch/zip(_:_:_:)-2m7ki.md)
  Combines elements from three other publishers and delivers groups of elements as tuples.
- [func zip<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.Zip3<Self, P, Q>, T>](publishers/catch/zip(_:_:_:)-cvsg.md)
  Combines elements from two other publishers and delivers a transformed output.
- [func zip<P, Q, R, T>(P, Q, R, (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.Zip4<Self, P, Q, R>, T>](publishers/catch/zip(_:_:_:_:).md)
  Combines elements from three other publishers and delivers a transformed output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/catch/publisher-implementations)*