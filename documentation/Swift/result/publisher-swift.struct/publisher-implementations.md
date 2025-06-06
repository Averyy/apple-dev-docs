# Publisher Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var values: AsyncPublisher<Self>](result/publisher-swift.struct/values-31x58.md)
  The elements produced by the publisher, as an asynchronous sequence.
- [var values: AsyncThrowingPublisher<Self>](result/publisher-swift.struct/values-7yerq.md)
  The elements produced by the publisher, as a throwing asynchronous sequence.
### Instance Methods
- [func append(Self.Output...) -> Publishers.Concatenate<Self, Publishers.Sequence<[Self.Output], Self.Failure>>](result/publisher-swift.struct/append(_:).md)
  Appends a publisher’s output with the specified elements.
- [func assertNoFailure(String, file: StaticString, line: UInt) -> Publishers.AssertNoFailure<Self>](result/publisher-swift.struct/assertnofailure(_:file:line:).md)
  Raises a fatal error when its upstream publisher fails, and otherwise republishes all received input.
- [func assign(to: inout Published<Self.Output>.Publisher)](result/publisher-swift.struct/assign(to:).md)
  Republishes elements received from a publisher, by assigning them to a property marked as a publisher.
- [func assign<Root>(to: ReferenceWritableKeyPath<Root, Self.Output>, on: Root) -> AnyCancellable](result/publisher-swift.struct/assign(to:on:).md)
  Assigns each element from a publisher to a property on an object.
- [func breakpoint(receiveSubscription: ((any Subscription) -> Bool)?, receiveOutput: ((Self.Output) -> Bool)?, receiveCompletion: ((Subscribers.Completion<Self.Failure>) -> Bool)?) -> Publishers.Breakpoint<Self>](result/publisher-swift.struct/breakpoint(receivesubscription:receiveoutput:receivecompletion:).md)
  Raises a debugger signal when a provided closure needs to stop the process in the debugger.
- [func breakpointOnError() -> Publishers.Breakpoint<Self>](result/publisher-swift.struct/breakpointonerror.md)
  Raises a debugger signal upon receiving a failure.
- [func buffer(size: Int, prefetch: Publishers.PrefetchStrategy, whenFull: Publishers.BufferingStrategy<Self.Failure>) -> Publishers.Buffer<Self>](result/publisher-swift.struct/buffer(size:prefetch:whenfull:).md)
  Buffers elements received from an upstream publisher.
- [func `catch`<P>((Self.Failure) -> P) -> Publishers.Catch<Self, P>](result/publisher-swift.struct/catch(_:).md)
  Handles errors from an upstream publisher by replacing it with another publisher.
- [func collect(Int) -> Publishers.CollectByCount<Self>](result/publisher-swift.struct/collect(_:).md)
  Collects up to the specified number of elements, and then emits a single array of the collection.
- [func collect<S>(Publishers.TimeGroupingStrategy<S>, options: S.SchedulerOptions?) -> Publishers.CollectByTime<Self, S>](result/publisher-swift.struct/collect(_:options:).md)
  Collects elements by a given time-grouping strategy, and emits a single array of the collection.
- [func combineLatest<P>(P) -> Publishers.CombineLatest<Self, P>](result/publisher-swift.struct/combinelatest(_:).md)
  Subscribes to an additional publisher and publishes a tuple upon receiving output from either publisher.
- [func combineLatest<P, Q>(P, Q) -> Publishers.CombineLatest3<Self, P, Q>](result/publisher-swift.struct/combinelatest(_:_:)-7cw12.md)
  Subscribes to two additional publishers and publishes a tuple upon receiving output from any of the publishers.
- [func combineLatest<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.CombineLatest<Self, P>, T>](result/publisher-swift.struct/combinelatest(_:_:)-8hngz.md)
  Subscribes to an additional publisher and invokes a closure upon receiving output from either publisher.
- [func combineLatest<P, Q, R>(P, Q, R) -> Publishers.CombineLatest4<Self, P, Q, R>](result/publisher-swift.struct/combinelatest(_:_:_:)-20old.md)
  Subscribes to three additional publishers and publishes a tuple upon receiving output from any of the publishers.
- [func combineLatest<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.CombineLatest3<Self, P, Q>, T>](result/publisher-swift.struct/combinelatest(_:_:_:)-9bqz.md)
  Subscribes to two additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R, T>(P, Q, R, (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.CombineLatest4<Self, P, Q, R>, T>](result/publisher-swift.struct/combinelatest(_:_:_:_:).md)
  Subscribes to three additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func compactMap<T>((Self.Output) -> T?) -> Publishers.CompactMap<Self, T>](result/publisher-swift.struct/compactmap(_:).md)
  Calls a closure with each received element and publishes any returned optional that has a value.
- [func contains(Self.Output) -> Publishers.Contains<Self>](result/publisher-swift.struct/contains(_:)-895n0.md)
  Publishes a Boolean value upon receiving an element equal to the argument.
- [func debounce<S>(for: S.SchedulerTimeType.Stride, scheduler: S, options: S.SchedulerOptions?) -> Publishers.Debounce<Self, S>](result/publisher-swift.struct/debounce(for:scheduler:options:).md)
  Publishes elements only after a specified time interval elapses between events.
- [func decode<Item, Coder>(type: Item.Type, decoder: Coder) -> Publishers.Decode<Self, Item, Coder>](result/publisher-swift.struct/decode(type:decoder:).md)
  Decodes the output from the upstream using a specified decoder.
- [func delay<S>(for: S.SchedulerTimeType.Stride, tolerance: S.SchedulerTimeType.Stride?, scheduler: S, options: S.SchedulerOptions?) -> Publishers.Delay<Self, S>](result/publisher-swift.struct/delay(for:tolerance:scheduler:options:).md)
  Delays delivery of all output to the downstream receiver by a specified amount of time on a particular scheduler.
- [func drop<P>(untilOutputFrom: P) -> Publishers.DropUntilOutput<Self, P>](result/publisher-swift.struct/drop(untiloutputfrom:).md)
  Ignores elements from the upstream publisher until it receives an element from a second publisher.
- [func drop(while: (Self.Output) -> Bool) -> Publishers.DropWhile<Self>](result/publisher-swift.struct/drop(while:).md)
  Omits elements from the upstream publisher until a given closure returns false, before republishing all remaining elements.
- [func dropFirst(Int) -> Publishers.Drop<Self>](result/publisher-swift.struct/dropfirst(_:).md)
  Omits the specified number of elements before republishing subsequent elements.
- [func encode<Coder>(encoder: Coder) -> Publishers.Encode<Self, Coder>](result/publisher-swift.struct/encode(encoder:).md)
  Encodes the output from upstream using a specified encoder.
- [func eraseToAnyPublisher() -> AnyPublisher<Self.Output, Self.Failure>](result/publisher-swift.struct/erasetoanypublisher.md)
  Wraps this publisher with a type eraser.
- [func filter((Self.Output) -> Bool) -> Publishers.Filter<Self>](result/publisher-swift.struct/filter(_:).md)
  Republishes all elements that match a provided closure.
- [func first(where: (Self.Output) -> Bool) -> Publishers.FirstWhere<Self>](result/publisher-swift.struct/first(where:).md)
  Publishes the first element of a stream to satisfy a predicate closure, then finishes normally.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](result/publisher-swift.struct/flatmap(maxpublishers:_:)-3jisi.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<Publishers.SetFailureType<P, Self.Failure>, Self>](result/publisher-swift.struct/flatmap(maxpublishers:_:)-4wm8q.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Publishers.SetFailureType<Self, P.Failure>>](result/publisher-swift.struct/flatmap(maxpublishers:_:)-53wvm.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<T, P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](result/publisher-swift.struct/flatmap(maxpublishers:_:)-9ddzt.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func handleEvents(receiveSubscription: ((any Subscription) -> Void)?, receiveOutput: ((Self.Output) -> Void)?, receiveCompletion: ((Subscribers.Completion<Self.Failure>) -> Void)?, receiveCancel: (() -> Void)?, receiveRequest: ((Subscribers.Demand) -> Void)?) -> Publishers.HandleEvents<Self>](result/publisher-swift.struct/handleevents(receivesubscription:receiveoutput:receivecompletion:receivecancel:receiverequest:).md)
  Performs the specified closures when publisher events occur.
- [func last(where: (Self.Output) -> Bool) -> Publishers.LastWhere<Self>](result/publisher-swift.struct/last(where:).md)
  Publishes the last element of a stream that satisfies a predicate closure, after upstream finishes.
- [func makeConnectable() -> Publishers.MakeConnectable<Self>](result/publisher-swift.struct/makeconnectable.md)
  Creates a connectable wrapper around the publisher.
- [func map<T>((Self.Output) -> T) -> Publishers.Map<Self, T>](result/publisher-swift.struct/map(_:)-4pr1v.md)
  Transforms all elements from the upstream publisher with a provided closure.
- [func map<T>(KeyPath<Self.Output, T>) -> Publishers.MapKeyPath<Self, T>](result/publisher-swift.struct/map(_:)-re9c.md)
  Publishes the value of a key path.
- [func map<T0, T1>(KeyPath<Self.Output, T0>, KeyPath<Self.Output, T1>) -> Publishers.MapKeyPath2<Self, T0, T1>](result/publisher-swift.struct/map(_:_:).md)
  Publishes the values of two key paths as a tuple.
- [func map<T0, T1, T2>(KeyPath<Self.Output, T0>, KeyPath<Self.Output, T1>, KeyPath<Self.Output, T2>) -> Publishers.MapKeyPath3<Self, T0, T1, T2>](result/publisher-swift.struct/map(_:_:_:).md)
  Publishes the values of three key paths as a tuple.
- [func mapError<E>((Self.Failure) -> E) -> Publishers.MapError<Self, E>](result/publisher-swift.struct/maperror(_:)-48hc7.md)
  Converts any failure from the upstream publisher into a new error.
- [func max() -> Publishers.Comparison<Self>](result/publisher-swift.struct/max-1vow5.md)
  Publishes the maximum value received from the upstream publisher, after it finishes.
- [func measureInterval<S>(using: S, options: S.SchedulerOptions?) -> Publishers.MeasureInterval<Self, S>](result/publisher-swift.struct/measureinterval(using:options:).md)
  Measures and emits the time interval between events received from an upstream publisher.
- [func merge(with: Self) -> Publishers.MergeMany<Self>](result/publisher-swift.struct/merge(with:).md)
  Combines elements from this publisher with those from another publisher of the same type, delivering an interleaved sequence of elements.
- [func merge<B, C>(with: B, C) -> Publishers.Merge3<Self, B, C>](result/publisher-swift.struct/merge(with:_:).md)
  Combines elements from this publisher with those from two other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D>(with: B, C, D) -> Publishers.Merge4<Self, B, C, D>](result/publisher-swift.struct/merge(with:_:_:).md)
  Combines elements from this publisher with those from three other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E>(with: B, C, D, E) -> Publishers.Merge5<Self, B, C, D, E>](result/publisher-swift.struct/merge(with:_:_:_:).md)
  Combines elements from this publisher with those from four other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F>(with: B, C, D, E, F) -> Publishers.Merge6<Self, B, C, D, E, F>](result/publisher-swift.struct/merge(with:_:_:_:_:).md)
  Combines elements from this publisher with those from five other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F, G>(with: B, C, D, E, F, G) -> Publishers.Merge7<Self, B, C, D, E, F, G>](result/publisher-swift.struct/merge(with:_:_:_:_:_:).md)
  Combines elements from this publisher with those from six other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F, G, H>(with: B, C, D, E, F, G, H) -> Publishers.Merge8<Self, B, C, D, E, F, G, H>](result/publisher-swift.struct/merge(with:_:_:_:_:_:_:).md)
  Combines elements from this publisher with those from seven other publishers, delivering an interleaved sequence of elements.
- [func min() -> Publishers.Comparison<Self>](result/publisher-swift.struct/min-69qqr.md)
  Publishes the minimum value received from the upstream publisher, after it finishes.
- [func multicast<S>(() -> S) -> Publishers.Multicast<Self, S>](result/publisher-swift.struct/multicast(_:).md)
  Applies a closure to create a subject that delivers elements to subscribers.
- [func multicast<S>(subject: S) -> Publishers.Multicast<Self, S>](result/publisher-swift.struct/multicast(subject:).md)
  Provides a subject to deliver elements to multiple subscribers.
- [func output(at: Int) -> Publishers.Output<Self>](result/publisher-swift.struct/output(at:).md)
  Publishes a specific element, indicated by its index in the sequence of published elements.
- [func output<R>(in: R) -> Publishers.Output<Self>](result/publisher-swift.struct/output(in:).md)
  Publishes elements specified by their range in the sequence of published elements.
- [func prefix(Int) -> Publishers.Output<Self>](result/publisher-swift.struct/prefix(_:).md)
  Republishes elements up to the specified maximum count.
- [func prefix<P>(untilOutputFrom: P) -> Publishers.PrefixUntilOutput<Self, P>](result/publisher-swift.struct/prefix(untiloutputfrom:).md)
  Republishes elements until another publisher emits an element.
- [func prefix(while: (Self.Output) -> Bool) -> Publishers.PrefixWhile<Self>](result/publisher-swift.struct/prefix(while:).md)
  Republishes elements while a predicate closure indicates publishing should continue.
- [func prepend(Self.Output...) -> Publishers.Concatenate<Publishers.Sequence<[Self.Output], Self.Failure>, Self>](result/publisher-swift.struct/prepend(_:).md)
  Prefixes a publisher’s output with the specified values.
- [func print(String, to: (any TextOutputStream)?) -> Publishers.Print<Self>](result/publisher-swift.struct/print(_:to:).md)
  Prints log messages for all publishing events.
- [func receive<S>(on: S, options: S.SchedulerOptions?) -> Publishers.ReceiveOn<Self, S>](result/publisher-swift.struct/receive(on:options:).md)
  Specifies the scheduler on which to receive elements from the publisher.
- [func reduce<T>(T, (T, Self.Output) -> T) -> Publishers.Reduce<Self, T>](result/publisher-swift.struct/reduce(_:_:)-2f2qa.md)
  Applies a closure that collects each element of a stream and publishes a final result upon completion.
- [func removeDuplicates() -> Publishers.RemoveDuplicates<Self>](result/publisher-swift.struct/removeduplicates-avx0.md)
  Publishes only elements that don’t match the previous element.
- [func replaceNil<T>(with: T) -> Publishers.Map<Self, T>](result/publisher-swift.struct/replacenil(with:).md)
  Replaces nil elements in the stream with the provided element.
- [func scan<T>(T, (T, Self.Output) -> T) -> Publishers.Scan<Self, T>](result/publisher-swift.struct/scan(_:_:)-6pykh.md)
  Transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [func setFailureType<E>(to: E.Type) -> Publishers.SetFailureType<Self, E>](result/publisher-swift.struct/setfailuretype(to:)-29p8s.md)
  Changes the failure type declared by the upstream publisher.
- [func share() -> Publishers.Share<Self>](result/publisher-swift.struct/share.md)
  Shares the output of an upstream publisher with multiple subscribers.
- [func sink(receiveCompletion: (Subscribers.Completion<Self.Failure>) -> Void, receiveValue: (Self.Output) -> Void) -> AnyCancellable](result/publisher-swift.struct/sink(receivecompletion:receivevalue:).md)
  Attaches a subscriber with closure-based behavior.
- [func sink(receiveValue: (Self.Output) -> Void) -> AnyCancellable](result/publisher-swift.struct/sink(receivevalue:).md)
  Attaches a subscriber with closure-based behavior to a publisher that never fails.
- [func subscribe<S>(S)](result/publisher-swift.struct/subscribe(_:)-70txi.md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S) -> AnyCancellable](result/publisher-swift.struct/subscribe(_:)-7c5ul.md)
  Attaches the specified subject to this publisher.
- [func subscribe<S>(on: S, options: S.SchedulerOptions?) -> Publishers.SubscribeOn<Self, S>](result/publisher-swift.struct/subscribe(on:options:).md)
  Specifies the scheduler on which to perform subscribe, cancel, and request operations.
- [func switchToLatest() -> Publishers.SwitchToLatest<Self.Output, Publishers.SetFailureType<Self, Self.Output.Failure>>](result/publisher-swift.struct/switchtolatest.md)
  Republishes elements sent by the most recently received publisher.
- [func throttle<S>(for: S.SchedulerTimeType.Stride, scheduler: S, latest: Bool) -> Publishers.Throttle<Self, S>](result/publisher-swift.struct/throttle(for:scheduler:latest:).md)
  Publishes either the most-recent or first element published by the upstream publisher in the specified time interval.
- [func timeout<S>(S.SchedulerTimeType.Stride, scheduler: S, options: S.SchedulerOptions?, customError: (() -> Self.Failure)?) -> Publishers.Timeout<Self, S>](result/publisher-swift.struct/timeout(_:scheduler:options:customerror:).md)
  Terminates publishing if the upstream publisher exceeds the specified time interval without producing an element.
- [func tryCatch<P>((Self.Failure) throws -> P) -> Publishers.TryCatch<Self, P>](result/publisher-swift.struct/trycatch(_:).md)
  Handles errors from an upstream publisher by either replacing it with another publisher or throwing a new error.
- [func tryCompactMap<T>((Self.Output) throws -> T?) -> Publishers.TryCompactMap<Self, T>](result/publisher-swift.struct/trycompactmap(_:).md)
  Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [func tryDrop(while: (Self.Output) throws -> Bool) -> Publishers.TryDropWhile<Self>](result/publisher-swift.struct/trydrop(while:).md)
  Omits elements from the upstream publisher until an error-throwing closure returns false, before republishing all remaining elements.
- [func tryFilter((Self.Output) throws -> Bool) -> Publishers.TryFilter<Self>](result/publisher-swift.struct/tryfilter(_:).md)
  Republishes all elements that match a provided error-throwing closure.
- [func tryFirst(where: (Self.Output) throws -> Bool) -> Publishers.TryFirstWhere<Self>](result/publisher-swift.struct/tryfirst(where:).md)
  Publishes the first element of a stream to satisfy a throwing predicate closure, then finishes normally.
- [func tryLast(where: (Self.Output) throws -> Bool) -> Publishers.TryLastWhere<Self>](result/publisher-swift.struct/trylast(where:).md)
  Publishes the last element of a stream that satisfies an error-throwing predicate closure, after the stream finishes.
- [func tryMap<T>((Self.Output) throws -> T) -> Publishers.TryMap<Self, T>](result/publisher-swift.struct/trymap(_:)-16sv7.md)
  Transforms all elements from the upstream publisher with a provided error-throwing closure.
- [func tryPrefix(while: (Self.Output) throws -> Bool) -> Publishers.TryPrefixWhile<Self>](result/publisher-swift.struct/tryprefix(while:).md)
  Republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [func tryReduce<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryReduce<Self, T>](result/publisher-swift.struct/tryreduce(_:_:)-3837a.md)
  Applies an error-throwing closure that collects each element of a stream and publishes a final result upon completion.
- [func tryScan<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryScan<Self, T>](result/publisher-swift.struct/tryscan(_:_:)-1pgp5.md)
  Transforms elements from the upstream publisher by providing the current element to an error-throwing closure along with the last value returned by the closure.
- [func zip<P>(P) -> Publishers.Zip<Self, P>](result/publisher-swift.struct/zip(_:).md)
  Combines elements from another publisher and deliver pairs of elements as tuples.
- [func zip<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.Zip<Self, P>, T>](result/publisher-swift.struct/zip(_:_:)-2ujx7.md)
  Combines elements from another publisher and delivers a transformed output.
- [func zip<P, Q>(P, Q) -> Publishers.Zip3<Self, P, Q>](result/publisher-swift.struct/zip(_:_:)-8pfav.md)
  Combines elements from two other publishers and delivers groups of elements as tuples.
- [func zip<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.Zip3<Self, P, Q>, T>](result/publisher-swift.struct/zip(_:_:_:)-55kzt.md)
  Combines elements from two other publishers and delivers a transformed output.
- [func zip<P, Q, R>(P, Q, R) -> Publishers.Zip4<Self, P, Q, R>](result/publisher-swift.struct/zip(_:_:_:)-5dx7l.md)
  Combines elements from three other publishers and delivers groups of elements as tuples.
- [func zip<P, Q, R, T>(P, Q, R, (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.Zip4<Self, P, Q, R>, T>](result/publisher-swift.struct/zip(_:_:_:_:).md)
  Combines elements from three other publishers and delivers a transformed output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/publisher-swift.struct/publisher-implementations)*