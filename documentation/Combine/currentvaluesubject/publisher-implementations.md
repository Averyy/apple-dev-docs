# Publisher Implementations

**Framework**: Combine

## Topics

### Instance Properties
- [var values: AsyncPublisher<Self>](currentvaluesubject/values-1t7gw.md)
  The elements produced by the publisher, as an asynchronous sequence.
- [var values: AsyncThrowingPublisher<Self>](currentvaluesubject/values-2swpi.md)
  The elements produced by the publisher, as a throwing asynchronous sequence.
### Instance Methods
- [func allSatisfy((Self.Output) -> Bool) -> Publishers.AllSatisfy<Self>](currentvaluesubject/allsatisfy(_:).md)
  Publishes a single Boolean value that indicates whether all received elements pass a given predicate.
- [func append<S>(S) -> Publishers.Concatenate<Self, Publishers.Sequence<S, Self.Failure>>](currentvaluesubject/append(_:)-1c71e.md)
  Appends a publisher’s output with the specified sequence.
- [func append(Self.Output...) -> Publishers.Concatenate<Self, Publishers.Sequence<[Self.Output], Self.Failure>>](currentvaluesubject/append(_:)-6r2d.md)
  Appends a publisher’s output with the specified elements.
- [func append<P>(P) -> Publishers.Concatenate<Self, P>](currentvaluesubject/append(_:)-7e3s0.md)
  Appends the output of this publisher with the elements emitted by the given publisher.
- [func assertNoFailure(String, file: StaticString, line: UInt) -> Publishers.AssertNoFailure<Self>](currentvaluesubject/assertnofailure(_:file:line:).md)
  Raises a fatal error when its upstream publisher fails, and otherwise republishes all received input.
- [func assign(to: inout Published<Self.Output>.Publisher)](currentvaluesubject/assign(to:).md)
  Republishes elements received from a publisher, by assigning them to a property marked as a publisher.
- [func assign<Root>(to: ReferenceWritableKeyPath<Root, Self.Output>, on: Root) -> AnyCancellable](currentvaluesubject/assign(to:on:).md)
  Assigns each element from a publisher to a property on an object.
- [func breakpoint(receiveSubscription: ((any Subscription) -> Bool)?, receiveOutput: ((Self.Output) -> Bool)?, receiveCompletion: ((Subscribers.Completion<Self.Failure>) -> Bool)?) -> Publishers.Breakpoint<Self>](currentvaluesubject/breakpoint(receivesubscription:receiveoutput:receivecompletion:).md)
  Raises a debugger signal when a provided closure needs to stop the process in the debugger.
- [func breakpointOnError() -> Publishers.Breakpoint<Self>](currentvaluesubject/breakpointonerror.md)
  Raises a debugger signal upon receiving a failure.
- [func buffer(size: Int, prefetch: Publishers.PrefetchStrategy, whenFull: Publishers.BufferingStrategy<Self.Failure>) -> Publishers.Buffer<Self>](currentvaluesubject/buffer(size:prefetch:whenfull:).md)
  Buffers elements received from an upstream publisher.
- [func `catch`<P>((Self.Failure) -> P) -> Publishers.Catch<Self, P>](currentvaluesubject/catch(_:).md)
  Handles errors from an upstream publisher by replacing it with another publisher.
- [func collect() -> Publishers.Collect<Self>](currentvaluesubject/collect.md)
  Collects all received elements, and emits a single array of the collection when the upstream publisher finishes.
- [func collect(Int) -> Publishers.CollectByCount<Self>](currentvaluesubject/collect(_:).md)
  Collects up to the specified number of elements, and then emits a single array of the collection.
- [func collect<S>(Publishers.TimeGroupingStrategy<S>, options: S.SchedulerOptions?) -> Publishers.CollectByTime<Self, S>](currentvaluesubject/collect(_:options:).md)
  Collects elements by a given time-grouping strategy, and emits a single array of the collection.
- [func combineLatest<P>(P) -> Publishers.CombineLatest<Self, P>](currentvaluesubject/combinelatest(_:).md)
  Subscribes to an additional publisher and publishes a tuple upon receiving output from either publisher.
- [func combineLatest<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.CombineLatest<Self, P>, T>](currentvaluesubject/combinelatest(_:_:)-1pkm7.md)
  Subscribes to an additional publisher and invokes a closure upon receiving output from either publisher.
- [func combineLatest<P, Q>(P, Q) -> Publishers.CombineLatest3<Self, P, Q>](currentvaluesubject/combinelatest(_:_:)-7grcc.md)
  Subscribes to two additional publishers and publishes a tuple upon receiving output from any of the publishers.
- [func combineLatest<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.CombineLatest3<Self, P, Q>, T>](currentvaluesubject/combinelatest(_:_:_:)-4u36w.md)
  Subscribes to two additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R>(P, Q, R) -> Publishers.CombineLatest4<Self, P, Q, R>](currentvaluesubject/combinelatest(_:_:_:)-9b93j.md)
  Subscribes to three additional publishers and publishes a tuple upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R, T>(P, Q, R, (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.CombineLatest4<Self, P, Q, R>, T>](currentvaluesubject/combinelatest(_:_:_:_:).md)
  Subscribes to three additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func compactMap<T>((Self.Output) -> T?) -> Publishers.CompactMap<Self, T>](currentvaluesubject/compactmap(_:).md)
  Calls a closure with each received element and publishes any returned optional that has a value.
- [func contains(Self.Output) -> Publishers.Contains<Self>](currentvaluesubject/contains(_:).md)
  Publishes a Boolean value upon receiving an element equal to the argument.
- [func contains(where: (Self.Output) -> Bool) -> Publishers.ContainsWhere<Self>](currentvaluesubject/contains(where:).md)
  Publishes a Boolean value upon receiving an element that satisfies the predicate closure.
- [func count() -> Publishers.Count<Self>](currentvaluesubject/count.md)
  Publishes the number of elements received from the upstream publisher.
- [func debounce<S>(for: S.SchedulerTimeType.Stride, scheduler: S, options: S.SchedulerOptions?) -> Publishers.Debounce<Self, S>](currentvaluesubject/debounce(for:scheduler:options:).md)
  Publishes elements only after a specified time interval elapses between events.
- [func decode<Item, Coder>(type: Item.Type, decoder: Coder) -> Publishers.Decode<Self, Item, Coder>](currentvaluesubject/decode(type:decoder:).md)
  Decodes the output from the upstream using a specified decoder.
- [func delay<S>(for: S.SchedulerTimeType.Stride, tolerance: S.SchedulerTimeType.Stride?, scheduler: S, options: S.SchedulerOptions?) -> Publishers.Delay<Self, S>](currentvaluesubject/delay(for:tolerance:scheduler:options:).md)
  Delays delivery of all output to the downstream receiver by a specified amount of time on a particular scheduler.
- [func drop<P>(untilOutputFrom: P) -> Publishers.DropUntilOutput<Self, P>](currentvaluesubject/drop(untiloutputfrom:).md)
  Ignores elements from the upstream publisher until it receives an element from a second publisher.
- [func drop(while: (Self.Output) -> Bool) -> Publishers.DropWhile<Self>](currentvaluesubject/drop(while:).md)
  Omits elements from the upstream publisher until a given closure returns false, before republishing all remaining elements.
- [func dropFirst(Int) -> Publishers.Drop<Self>](currentvaluesubject/dropfirst(_:).md)
  Omits the specified number of elements before republishing subsequent elements.
- [func encode<Coder>(encoder: Coder) -> Publishers.Encode<Self, Coder>](currentvaluesubject/encode(encoder:).md)
  Encodes the output from upstream using a specified encoder.
- [func eraseToAnyPublisher() -> AnyPublisher<Self.Output, Self.Failure>](currentvaluesubject/erasetoanypublisher.md)
  Wraps this publisher with a type eraser.
- [func filter((Self.Output) -> Bool) -> Publishers.Filter<Self>](currentvaluesubject/filter(_:).md)
  Republishes all elements that match a provided closure.
- [func first() -> Publishers.First<Self>](currentvaluesubject/first.md)
  Publishes the first element of a stream, then finishes.
- [func first(where: (Self.Output) -> Bool) -> Publishers.FirstWhere<Self>](currentvaluesubject/first(where:).md)
  Publishes the first element of a stream to satisfy a predicate closure, then finishes normally.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<Publishers.SetFailureType<P, Self.Failure>, Self>](currentvaluesubject/flatmap(maxpublishers:_:)-17ono.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Publishers.SetFailureType<Self, P.Failure>>](currentvaluesubject/flatmap(maxpublishers:_:)-38nry.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<T, P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](currentvaluesubject/flatmap(maxpublishers:_:)-4djtb.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](currentvaluesubject/flatmap(maxpublishers:_:)-6tj09.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func handleEvents(receiveSubscription: ((any Subscription) -> Void)?, receiveOutput: ((Self.Output) -> Void)?, receiveCompletion: ((Subscribers.Completion<Self.Failure>) -> Void)?, receiveCancel: (() -> Void)?, receiveRequest: ((Subscribers.Demand) -> Void)?) -> Publishers.HandleEvents<Self>](currentvaluesubject/handleevents(receivesubscription:receiveoutput:receivecompletion:receivecancel:receiverequest:).md)
  Performs the specified closures when publisher events occur.
- [func ignoreOutput() -> Publishers.IgnoreOutput<Self>](currentvaluesubject/ignoreoutput.md)
  Ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [func last() -> Publishers.Last<Self>](currentvaluesubject/last.md)
  Publishes the last element of a stream, after the stream finishes.
- [func last(where: (Self.Output) -> Bool) -> Publishers.LastWhere<Self>](currentvaluesubject/last(where:).md)
  Publishes the last element of a stream that satisfies a predicate closure, after upstream finishes.
- [func makeConnectable() -> Publishers.MakeConnectable<Self>](currentvaluesubject/makeconnectable.md)
  Creates a connectable wrapper around the publisher.
- [func map<T>((Self.Output) -> T) -> Publishers.Map<Self, T>](currentvaluesubject/map(_:)-762uk.md)
  Transforms all elements from the upstream publisher with a provided closure.
- [func map<T>(KeyPath<Self.Output, T>) -> Publishers.MapKeyPath<Self, T>](currentvaluesubject/map(_:)-hyaf.md)
  Publishes the value of a key path.
- [func map<T0, T1>(KeyPath<Self.Output, T0>, KeyPath<Self.Output, T1>) -> Publishers.MapKeyPath2<Self, T0, T1>](currentvaluesubject/map(_:_:).md)
  Publishes the values of two key paths as a tuple.
- [func map<T0, T1, T2>(KeyPath<Self.Output, T0>, KeyPath<Self.Output, T1>, KeyPath<Self.Output, T2>) -> Publishers.MapKeyPath3<Self, T0, T1, T2>](currentvaluesubject/map(_:_:_:).md)
  Publishes the values of three key paths as a tuple.
- [func mapError<E>((Self.Failure) -> E) -> Publishers.MapError<Self, E>](currentvaluesubject/maperror(_:).md)
  Converts any failure from the upstream publisher into a new error.
- [func max() -> Publishers.Comparison<Self>](currentvaluesubject/max.md)
  Publishes the maximum value received from the upstream publisher, after it finishes.
- [func max(by: (Self.Output, Self.Output) -> Bool) -> Publishers.Comparison<Self>](currentvaluesubject/max(by:).md)
  Publishes the maximum value received from the upstream publisher, using the provided ordering closure.
- [func measureInterval<S>(using: S, options: S.SchedulerOptions?) -> Publishers.MeasureInterval<Self, S>](currentvaluesubject/measureinterval(using:options:).md)
  Measures and emits the time interval between events received from an upstream publisher.
- [func merge<P>(with: P) -> Publishers.Merge<Self, P>](currentvaluesubject/merge(with:)-92f2c.md)
  Combines elements from this publisher with those from another publisher, delivering an interleaved sequence of elements.
- [func merge(with: Self) -> Publishers.MergeMany<Self>](currentvaluesubject/merge(with:)-9a0eq.md)
  Combines elements from this publisher with those from another publisher of the same type, delivering an interleaved sequence of elements.
- [func merge<B, C>(with: B, C) -> Publishers.Merge3<Self, B, C>](currentvaluesubject/merge(with:_:).md)
  Combines elements from this publisher with those from two other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D>(with: B, C, D) -> Publishers.Merge4<Self, B, C, D>](currentvaluesubject/merge(with:_:_:).md)
  Combines elements from this publisher with those from three other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E>(with: B, C, D, E) -> Publishers.Merge5<Self, B, C, D, E>](currentvaluesubject/merge(with:_:_:_:).md)
  Combines elements from this publisher with those from four other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F>(with: B, C, D, E, F) -> Publishers.Merge6<Self, B, C, D, E, F>](currentvaluesubject/merge(with:_:_:_:_:).md)
  Combines elements from this publisher with those from five other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F, G>(with: B, C, D, E, F, G) -> Publishers.Merge7<Self, B, C, D, E, F, G>](currentvaluesubject/merge(with:_:_:_:_:_:).md)
  Combines elements from this publisher with those from six other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F, G, H>(with: B, C, D, E, F, G, H) -> Publishers.Merge8<Self, B, C, D, E, F, G, H>](currentvaluesubject/merge(with:_:_:_:_:_:_:).md)
  Combines elements from this publisher with those from seven other publishers, delivering an interleaved sequence of elements.
- [func min() -> Publishers.Comparison<Self>](currentvaluesubject/min.md)
  Publishes the minimum value received from the upstream publisher, after it finishes.
- [func min(by: (Self.Output, Self.Output) -> Bool) -> Publishers.Comparison<Self>](currentvaluesubject/min(by:).md)
  Publishes the minimum value received from the upstream publisher, after it finishes.
- [func multicast<S>(() -> S) -> Publishers.Multicast<Self, S>](currentvaluesubject/multicast(_:).md)
  Applies a closure to create a subject that delivers elements to subscribers.
- [func multicast<S>(subject: S) -> Publishers.Multicast<Self, S>](currentvaluesubject/multicast(subject:).md)
  Provides a subject to deliver elements to multiple subscribers.
- [func output(at: Int) -> Publishers.Output<Self>](currentvaluesubject/output(at:).md)
  Publishes a specific element, indicated by its index in the sequence of published elements.
- [func output<R>(in: R) -> Publishers.Output<Self>](currentvaluesubject/output(in:).md)
  Publishes elements specified by their range in the sequence of published elements.
- [func prefix(Int) -> Publishers.Output<Self>](currentvaluesubject/prefix(_:).md)
  Republishes elements up to the specified maximum count.
- [func prefix<P>(untilOutputFrom: P) -> Publishers.PrefixUntilOutput<Self, P>](currentvaluesubject/prefix(untiloutputfrom:).md)
  Republishes elements until another publisher emits an element.
- [func prefix(while: (Self.Output) -> Bool) -> Publishers.PrefixWhile<Self>](currentvaluesubject/prefix(while:).md)
  Republishes elements while a predicate closure indicates publishing should continue.
- [func prepend(Self.Output...) -> Publishers.Concatenate<Publishers.Sequence<[Self.Output], Self.Failure>, Self>](currentvaluesubject/prepend(_:)-6nhqk.md)
  Prefixes a publisher’s output with the specified values.
- [func prepend<S>(S) -> Publishers.Concatenate<Publishers.Sequence<S, Self.Failure>, Self>](currentvaluesubject/prepend(_:)-948yd.md)
  Prefixes a publisher’s output with the specified sequence.
- [func prepend<P>(P) -> Publishers.Concatenate<P, Self>](currentvaluesubject/prepend(_:)-9b032.md)
  Prefixes the output of this publisher with the elements emitted by the given publisher.
- [func print(String, to: (any TextOutputStream)?) -> Publishers.Print<Self>](currentvaluesubject/print(_:to:).md)
  Prints log messages for all publishing events.
- [func receive<S>(on: S, options: S.SchedulerOptions?) -> Publishers.ReceiveOn<Self, S>](currentvaluesubject/receive(on:options:).md)
  Specifies the scheduler on which to receive elements from the publisher.
- [func reduce<T>(T, (T, Self.Output) -> T) -> Publishers.Reduce<Self, T>](currentvaluesubject/reduce(_:_:).md)
  Applies a closure that collects each element of a stream and publishes a final result upon completion.
- [func removeDuplicates() -> Publishers.RemoveDuplicates<Self>](currentvaluesubject/removeduplicates.md)
  Publishes only elements that don’t match the previous element.
- [func removeDuplicates(by: (Self.Output, Self.Output) -> Bool) -> Publishers.RemoveDuplicates<Self>](currentvaluesubject/removeduplicates(by:).md)
  Publishes only elements that don’t match the previous element, as evaluated by a provided closure.
- [func replaceEmpty(with: Self.Output) -> Publishers.ReplaceEmpty<Self>](currentvaluesubject/replaceempty(with:).md)
  Replaces an empty stream with the provided element.
- [func replaceError(with: Self.Output) -> Publishers.ReplaceError<Self>](currentvaluesubject/replaceerror(with:).md)
  Replaces any errors in the stream with the provided element.
- [func replaceNil<T>(with: T) -> Publishers.Map<Self, T>](currentvaluesubject/replacenil(with:).md)
  Replaces nil elements in the stream with the provided element.
- [func retry(Int) -> Publishers.Retry<Self>](currentvaluesubject/retry(_:).md)
  Attempts to recreate a failed subscription with the upstream publisher up to the number of times you specify.
- [func scan<T>(T, (T, Self.Output) -> T) -> Publishers.Scan<Self, T>](currentvaluesubject/scan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [func setFailureType<E>(to: E.Type) -> Publishers.SetFailureType<Self, E>](currentvaluesubject/setfailuretype(to:).md)
  Changes the failure type declared by the upstream publisher.
- [func share() -> Publishers.Share<Self>](currentvaluesubject/share.md)
  Shares the output of an upstream publisher with multiple subscribers.
- [func sink(receiveCompletion: (Subscribers.Completion<Self.Failure>) -> Void, receiveValue: (Self.Output) -> Void) -> AnyCancellable](currentvaluesubject/sink(receivecompletion:receivevalue:).md)
  Attaches a subscriber with closure-based behavior.
- [func sink(receiveValue: (Self.Output) -> Void) -> AnyCancellable](currentvaluesubject/sink(receivevalue:).md)
  Attaches a subscriber with closure-based behavior to a publisher that never fails.
- [func subscribe<S>(S)](currentvaluesubject/subscribe(_:)-2v9p8.md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S) -> AnyCancellable](currentvaluesubject/subscribe(_:)-6p0z8.md)
  Attaches the specified subject to this publisher.
- [func subscribe<S>(on: S, options: S.SchedulerOptions?) -> Publishers.SubscribeOn<Self, S>](currentvaluesubject/subscribe(on:options:).md)
  Specifies the scheduler on which to perform subscribe, cancel, and request operations.
- [func switchToLatest() -> Publishers.SwitchToLatest<Self.Output, Publishers.SetFailureType<Self, Self.Output.Failure>>](currentvaluesubject/switchtolatest.md)
  Republishes elements sent by the most recently received publisher.
- [func throttle<S>(for: S.SchedulerTimeType.Stride, scheduler: S, latest: Bool) -> Publishers.Throttle<Self, S>](currentvaluesubject/throttle(for:scheduler:latest:).md)
  Publishes either the most-recent or first element published by the upstream publisher in the specified time interval.
- [func timeout<S>(S.SchedulerTimeType.Stride, scheduler: S, options: S.SchedulerOptions?, customError: (() -> Self.Failure)?) -> Publishers.Timeout<Self, S>](currentvaluesubject/timeout(_:scheduler:options:customerror:).md)
  Terminates publishing if the upstream publisher exceeds the specified time interval without producing an element.
- [func tryAllSatisfy((Self.Output) throws -> Bool) -> Publishers.TryAllSatisfy<Self>](currentvaluesubject/tryallsatisfy(_:).md)
  Publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.
- [func tryCatch<P>((Self.Failure) throws -> P) -> Publishers.TryCatch<Self, P>](currentvaluesubject/trycatch(_:).md)
  Handles errors from an upstream publisher by either replacing it with another publisher or throwing a new error.
- [func tryCompactMap<T>((Self.Output) throws -> T?) -> Publishers.TryCompactMap<Self, T>](currentvaluesubject/trycompactmap(_:).md)
  Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [func tryContains(where: (Self.Output) throws -> Bool) -> Publishers.TryContainsWhere<Self>](currentvaluesubject/trycontains(where:).md)
  Publishes a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [func tryDrop(while: (Self.Output) throws -> Bool) -> Publishers.TryDropWhile<Self>](currentvaluesubject/trydrop(while:).md)
  Omits elements from the upstream publisher until an error-throwing closure returns false, before republishing all remaining elements.
- [func tryFilter((Self.Output) throws -> Bool) -> Publishers.TryFilter<Self>](currentvaluesubject/tryfilter(_:).md)
  Republishes all elements that match a provided error-throwing closure.
- [func tryFirst(where: (Self.Output) throws -> Bool) -> Publishers.TryFirstWhere<Self>](currentvaluesubject/tryfirst(where:).md)
  Publishes the first element of a stream to satisfy a throwing predicate closure, then finishes normally.
- [func tryLast(where: (Self.Output) throws -> Bool) -> Publishers.TryLastWhere<Self>](currentvaluesubject/trylast(where:).md)
  Publishes the last element of a stream that satisfies an error-throwing predicate closure, after the stream finishes.
- [func tryMap<T>((Self.Output) throws -> T) -> Publishers.TryMap<Self, T>](currentvaluesubject/trymap(_:).md)
  Transforms all elements from the upstream publisher with a provided error-throwing closure.
- [func tryMax(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](currentvaluesubject/trymax(by:).md)
  Publishes the maximum value received from the upstream publisher, using the provided error-throwing closure to order the items.
- [func tryMin(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](currentvaluesubject/trymin(by:).md)
  Publishes the minimum value received from the upstream publisher, using the provided error-throwing closure to order the items.
- [func tryPrefix(while: (Self.Output) throws -> Bool) -> Publishers.TryPrefixWhile<Self>](currentvaluesubject/tryprefix(while:).md)
  Republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [func tryReduce<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryReduce<Self, T>](currentvaluesubject/tryreduce(_:_:).md)
  Applies an error-throwing closure that collects each element of a stream and publishes a final result upon completion.
- [func tryRemoveDuplicates(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryRemoveDuplicates<Self>](currentvaluesubject/tryremoveduplicates(by:).md)
  Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [func tryScan<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryScan<Self, T>](currentvaluesubject/tryscan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to an error-throwing closure along with the last value returned by the closure.
- [func zip<P>(P) -> Publishers.Zip<Self, P>](currentvaluesubject/zip(_:).md)
  Combines elements from another publisher and deliver pairs of elements as tuples.
- [func zip<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.Zip<Self, P>, T>](currentvaluesubject/zip(_:_:)-339hc.md)
  Combines elements from another publisher and delivers a transformed output.
- [func zip<P, Q>(P, Q) -> Publishers.Zip3<Self, P, Q>](currentvaluesubject/zip(_:_:)-6qsv3.md)
  Combines elements from two other publishers and delivers groups of elements as tuples.
- [func zip<P, Q, R>(P, Q, R) -> Publishers.Zip4<Self, P, Q, R>](currentvaluesubject/zip(_:_:_:)-1rq8b.md)
  Combines elements from three other publishers and delivers groups of elements as tuples.
- [func zip<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.Zip3<Self, P, Q>, T>](currentvaluesubject/zip(_:_:_:)-4nzo7.md)
  Combines elements from two other publishers and delivers a transformed output.
- [func zip<P, Q, R, T>(P, Q, R, (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.Zip4<Self, P, Q, R>, T>](currentvaluesubject/zip(_:_:_:_:).md)
  Combines elements from three other publishers and delivers a transformed output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/currentvaluesubject/publisher-implementations)*