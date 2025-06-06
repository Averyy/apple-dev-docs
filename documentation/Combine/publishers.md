# Publishers

**Framework**: Combine  
**Kind**: enum

A namespace for types that serve as publishers.

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
enum Publishers
```

#### Overview

The various operators defined as extensions on [`Publisher`](publisher.md) implement their functionality as classes or structures that extend this enumeration. For example, the `contains(_:)` operator returns a `Publishers.Contains` instance.

## Topics

### Convenience Publishers
- [Publishers.Sequence](publishers/sequence.md)
  A publisher that publishes a given sequence of elements.
- [Publishers.Catch](publishers/catch.md)
  A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher.
### Working with Subscribers
- [Publishers.ReceiveOn](publishers/receiveon.md)
  A publisher that delivers elements to its downstream subscriber on a specific scheduler.
- [Publishers.SubscribeOn](publishers/subscribeon.md)
  A publisher that receives elements from an upstream publisher on a specific scheduler.
### Mapping Elements
- [Publishers.Map](publishers/map.md)
  A publisher that transforms all elements from the upstream publisher with a provided closure.
- [Publishers.TryMap](publishers/trymap.md)
  A publisher that transforms all elements from the upstream publisher with a provided error-throwing closure.
- [Publishers.MapError](publishers/maperror.md)
  A publisher that converts any failure from the upstream publisher into a new error.
- [Publishers.Scan](publishers/scan.md)
  A publisher that transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [Publishers.TryScan](publishers/tryscan.md)
  A publisher that transforms elements from the upstream publisher by providing the current element to a failable closure along with the last value returned by the closure.
- [Publishers.SetFailureType](publishers/setfailuretype.md)
  A publisher that appears to send a specified failure type.
### Filtering Elements
- [Publishers.Filter](publishers/filter.md)
  A publisher that republishes all elements that match a provided closure.
- [Publishers.TryFilter](publishers/tryfilter.md)
  A publisher that republishes all elements that match a provided error-throwing closure.
- [Publishers.CompactMap](publishers/compactmap.md)
  A publisher that republishes all non-nil results of calling a closure with each received element.
- [Publishers.TryCompactMap](publishers/trycompactmap.md)
  A publisher that republishes all non-nil results of calling an error-throwing closure with each received element.
- [Publishers.RemoveDuplicates](publishers/removeduplicates.md)
  A publisher that publishes only elements that don’t match the previous element.
- [Publishers.TryRemoveDuplicates](publishers/tryremoveduplicates.md)
  A publisher that publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [Publishers.ReplaceEmpty](publishers/replaceempty.md)
  A publisher that replaces an empty stream with a provided element.
- [Publishers.ReplaceError](publishers/replaceerror.md)
  A publisher that replaces any errors in the stream with a provided element.
### Reducing Elements
- [Publishers.Collect](publishers/collect.md)
  A publisher that buffers items.
- [Publishers.CollectByCount](publishers/collectbycount.md)
  A publisher that buffers a maximum number of items.
- [Publishers.CollectByTime](publishers/collectbytime.md)
  A publisher that buffers and periodically publishes its items.
- [Publishers.TimeGroupingStrategy](publishers/timegroupingstrategy.md)
  A strategy for collecting received elements.
- [Publishers.IgnoreOutput](publishers/ignoreoutput.md)
  A publisher that ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [Publishers.Reduce](publishers/reduce.md)
  A publisher that applies a closure to all received elements and produces an accumulated value when the upstream publisher finishes.
- [Publishers.TryReduce](publishers/tryreduce.md)
  A publisher that applies an error-throwing closure to all received elements and produces an accumulated value when the upstream publisher finishes.
### Applying Mathematical Operations on Elements
- [Publishers.Count](publishers/count.md)
  A publisher that publishes the number of elements received from the upstream publisher.
- [Publishers.Comparison](publishers/comparison.md)
  A publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item.
- [Publishers.TryComparison](publishers/trycomparison.md)
  A publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item, and fails if the ordering logic throws an error.
### Applying Matching Criteria to Elements
- [Publishers.Contains](publishers/contains.md)
  A publisher that emits a Boolean value when it receives a specific element from its upstream publisher.
- [Publishers.ContainsWhere](publishers/containswhere.md)
  A publisher that emits a Boolean value upon receiving an element that satisfies the predicate closure.
- [Publishers.TryContainsWhere](publishers/trycontainswhere.md)
  A publisher that emits a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [Publishers.AllSatisfy](publishers/allsatisfy.md)
  A publisher that publishes a single Boolean value that indicates whether all received elements pass a given predicate.
- [Publishers.TryAllSatisfy](publishers/tryallsatisfy.md)
  A publisher that publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.
### Applying Sequence Operations to Elements
- [Publishers.DropUntilOutput](publishers/dropuntiloutput.md)
  A publisher that ignores elements from the upstream publisher until it receives an element from second publisher.
- [Publishers.Drop](publishers/drop.md)
  A publisher that omits a specified number of elements before republishing later elements.
- [Publishers.DropWhile](publishers/dropwhile.md)
  A publisher that omits elements from an upstream publisher until a given closure returns false.
- [Publishers.TryDropWhile](publishers/trydropwhile.md)
  A publisher that omits elements from an upstream publisher until a given error-throwing closure returns false.
- [Publishers.Concatenate](publishers/concatenate.md)
  A publisher that emits all of one publisher’s elements before those from another publisher.
- [Publishers.PrefixWhile](publishers/prefixwhile.md)
  A publisher that republishes elements while a predicate closure indicates publishing should continue.
- [Publishers.TryPrefixWhile](publishers/tryprefixwhile.md)
  A publisher that republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [Publishers.PrefixUntilOutput](publishers/prefixuntiloutput.md)
  A publisher that republishes elements until another publisher emits an element.
### Selecting Specific Elements
- [Publishers.First](publishers/first.md)
  A publisher that publishes the first element of a stream, then finishes.
- [Publishers.FirstWhere](publishers/firstwhere.md)
  A publisher that only publishes the first element of a stream to satisfy a predicate closure.
- [Publishers.TryFirstWhere](publishers/tryfirstwhere.md)
  A publisher that only publishes the first element of a stream to satisfy a throwing predicate closure.
- [Publishers.Last](publishers/last.md)
  A publisher that waits until after the stream finishes, and then publishes the last element of the stream.
- [Publishers.LastWhere](publishers/lastwhere.md)
  A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies a predicate closure.
- [Publishers.TryLastWhere](publishers/trylastwhere.md)
  A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies an error-throwing predicate closure.
- [Publishers.Output](publishers/output.md)
  A publisher that publishes elements specified by a range in the sequence of published elements.
### Combining Elements from Multiple Publishers
- [Publishers.CombineLatest](publishers/combinelatest.md)
  A publisher that receives and combines the latest elements from two publishers.
- [Publishers.CombineLatest3](publishers/combinelatest3.md)
  A publisher that receives and combines the latest elements from three publishers.
- [Publishers.CombineLatest4](publishers/combinelatest4.md)
  A publisher that receives and combines the latest elements from four publishers.
- [Publishers.Merge](publishers/merge.md)
  A publisher created by applying the merge function to two upstream publishers.
- [Publishers.Merge3](publishers/merge3.md)
  A publisher created by applying the merge function to three upstream publishers.
- [Publishers.Merge4](publishers/merge4.md)
  A publisher created by applying the merge function to four upstream publishers.
- [Publishers.Merge5](publishers/merge5.md)
  A publisher created by applying the merge function to five upstream publishers.
- [Publishers.Merge6](publishers/merge6.md)
  A publisher created by applying the merge function to six upstream publishers.
- [Publishers.Merge7](publishers/merge7.md)
  A publisher created by applying the merge function to seven upstream publishers.
- [Publishers.Merge8](publishers/merge8.md)
  A publisher created by applying the merge function to eight upstream publishers.
- [Publishers.MergeMany](publishers/mergemany.md)
  A publisher created by applying the merge function to an arbitrary number of upstream publishers.
- [Publishers.Zip](publishers/zip.md)
  A publisher created by applying the zip function to two upstream publishers.
- [Publishers.Zip3](publishers/zip3.md)
  A publisher created by applying the zip function to three upstream publishers.
- [Publishers.Zip4](publishers/zip4.md)
  A publisher created by applying the zip function to four upstream publishers.
### Republishing Elements by Subscribing to New Publishers
- [Publishers.FlatMap](publishers/flatmap.md)
  A publisher that transforms elements from an upstream publisher into a new publisher.
- [Publishers.SwitchToLatest](publishers/switchtolatest.md)
  A publisher that flattens nested publishers.
### Handling Errors
- [Publishers.AssertNoFailure](publishers/assertnofailure.md)
  A publisher that raises a fatal error upon receiving any failure, and otherwise republishes all received input.
- [Publishers.Catch](publishers/catch.md)
  A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher.
- [Publishers.TryCatch](publishers/trycatch.md)
  A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher or producing a new error.
- [Publishers.Retry](publishers/retry.md)
  A publisher that attempts to recreate its subscription to a failed upstream publisher.
### Controlling Timing
- [Publishers.MeasureInterval](publishers/measureinterval.md)
  A publisher that measures and emits the time interval between events received from an upstream publisher.
- [Publishers.Debounce](publishers/debounce.md)
  A publisher that publishes elements only after a specified time interval elapses between events.
- [Publishers.Delay](publishers/delay.md)
  A publisher that delays delivery of elements and completion to the downstream receiver.
- [Publishers.Throttle](publishers/throttle.md)
  A publisher that publishes either the most-recent or first element published by the upstream publisher in a specified time interval.
- [Publishers.Timeout](publishers/timeout.md)
  A publisher that terminates publishing if the upstream publisher exceeds a specified time interval without producing an element.
### Encoding and Decoding
- [Publishers.Decode](publishers/decode.md)
  A publisher that decodes elements received from an upstream publisher, using a given decoder.
- [Publishers.Encode](publishers/encode.md)
  A publisher that encodes elements received from an upstream publisher, using a given encoder.
### Identifying Properties with Key Paths
- [Publishers.MapKeyPath](publishers/mapkeypath.md)
  A publisher that publishes the value of a key path.
- [Publishers.MapKeyPath2](publishers/mapkeypath2.md)
  A publisher that publishes the values of two key paths as a tuple.
- [Publishers.MapKeyPath3](publishers/mapkeypath3.md)
  A publisher that publishes the values of three key paths as a tuple.
### Working with Multiple Subscribers
- [Publishers.Multicast](publishers/multicast.md)
  A publisher that uses a subject to deliver elements to multiple subscribers.
- [Publishers.Share](publishers/share.md)
  A publisher that shares the output of an upstream publisher with multiple subscribers.
### Buffering Elements
- [Publishers.Buffer](publishers/buffer.md)
  A publisher that buffers elements from an upstream publisher.
- [Publishers.BufferingStrategy](publishers/bufferingstrategy.md)
  A strategy that handles exhaustion of a buffer’s capacity.
- [Publishers.PrefetchStrategy](publishers/prefetchstrategy.md)
  A strategy for filling a buffer.
### Using Explicit Publisher Connections
- [Publishers.Autoconnect](publishers/autoconnect.md)
  A publisher that automatically connects to an upstream connectable publisher.
- [Publishers.MakeConnectable](publishers/makeconnectable.md)
  A publisher that provides explicit connectability to another publisher.
### Debugging
- [Publishers.Breakpoint](publishers/breakpoint.md)
  A publisher that raises a debugger signal when a provided closure needs to stop the process in the debugger.
- [Publishers.HandleEvents](publishers/handleevents.md)
  A publisher that performs the specified closures when publisher events occur.
- [Publishers.Print](publishers/print.md)
  A publisher that prints log messages for all publishing events, optionally prefixed with a given string.

## See Also

- [protocol Publisher](publisher.md)
  Declares that a type can transmit a sequence of values over time.
- [struct AnyPublisher](anypublisher.md)
  A publisher that performs type erasure by wrapping another publisher.
- [struct Published](published.md)
  A type that publishes a property marked with an attribute.
- [protocol Cancellable](cancellable.md)
  A protocol indicating that an activity or action supports cancellation.
- [class AnyCancellable](anycancellable.md)
  A type-erasing cancellable object that executes a provided closure when canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers)*