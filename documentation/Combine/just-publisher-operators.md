# Publisher Operators

**Framework**: Combine

Methods that create downstream publishers or subscribers to act on the elements they receive.

## Topics

### Mapping elements
- [func map<T>((Output) -> T) -> Just<T>](just/map(_:).md)
- [func tryMap<T>((Output) throws -> T) -> Result<T, any Error>.Publisher](just/trymap(_:).md)
- [func mapError<E>((Just<Output>.Failure) -> E) -> Result<Output, E>.Publisher](just/maperror(_:).md)
- [func scan<T>(T, (T, Output) -> T) -> Result<T, Just<Output>.Failure>.Publisher](just/scan(_:_:).md)
- [func tryScan<T>(T, (T, Output) throws -> T) -> Result<T, any Error>.Publisher](just/tryscan(_:_:).md)
- [func setFailureType<E>(to: E.Type) -> Result<Output, E>.Publisher](just/setfailuretype(to:).md)
### Filtering elements
- [func filter((Output) -> Bool) -> Optional<Output>.Publisher](just/filter(_:).md)
- [func compactMap<T>((Output) -> T?) -> Optional<T>.Publisher](just/compactmap(_:).md)
- [func removeDuplicates() -> Just<Output>](just/removeduplicates.md)
- [func removeDuplicates(by: (Output, Output) -> Bool) -> Just<Output>](just/removeduplicates(by:).md)
- [func tryRemoveDuplicates(by: (Output, Output) throws -> Bool) -> Result<Output, any Error>.Publisher](just/tryremoveduplicates(by:).md)
- [func replaceEmpty(with: Output) -> Just<Output>](just/replaceempty(with:).md)
- [func replaceError(with: Output) -> Just<Output>](just/replaceerror(with:).md)
### Reducing elements
- [func collect() -> Just<[Output]>](just/collect.md)
- [func ignoreOutput() -> Empty<Output, Just<Output>.Failure>](just/ignoreoutput.md)
- [func reduce<T>(T, (T, Output) -> T) -> Result<T, Just<Output>.Failure>.Publisher](just/reduce(_:_:).md)
- [func tryReduce<T>(T, (T, Output) throws -> T) -> Result<T, any Error>.Publisher](just/tryreduce(_:_:).md)
### Applying mathematical operations on elements
- [func count() -> Just<Int>](just/count.md)
- [func max() -> Just<Output>](just/max.md)
- [func max(by: (Output, Output) -> Bool) -> Just<Output>](just/max(by:).md)
- [func min() -> Just<Output>](just/min.md)
- [func min(by: (Output, Output) -> Bool) -> Just<Output>](just/min(by:).md)
### Applying matching criteria to elements
- [func contains(Output) -> Just<Bool>](just/contains(_:).md)
- [func contains(where: (Output) -> Bool) -> Just<Bool>](just/contains(where:).md)
- [func tryContains(where: (Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](just/trycontains(where:).md)
- [func allSatisfy((Output) -> Bool) -> Just<Bool>](just/allsatisfy(_:).md)
- [func tryAllSatisfy((Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](just/tryallsatisfy(_:).md)
### Applying sequence operations to elements
- [func dropFirst(Int) -> Optional<Output>.Publisher](just/dropfirst(_:).md)
- [func drop(while: (Output) -> Bool) -> Optional<Output>.Publisher](just/drop(while:).md)
- [func append(Output...) -> Publishers.Sequence<[Output], Just<Output>.Failure>](just/append(_:)-7eyqj.md)
- [func append<S>(S) -> Publishers.Sequence<[Output], Just<Output>.Failure>](just/append(_:)-7sxlu.md)
- [func prepend<S>(S) -> Publishers.Sequence<[Output], Just<Output>.Failure>](just/prepend(_:)-39e57.md)
- [func prepend(Output...) -> Publishers.Sequence<[Output], Just<Output>.Failure>](just/prepend(_:)-7fg73.md)
- [func prefix(Int) -> Optional<Output>.Publisher](just/prefix(_:).md)
- [func prefix(while: (Output) -> Bool) -> Optional<Output>.Publisher](just/prefix(while:).md)
### Selecting specific elements
- [func first() -> Just<Output>](just/first.md)
- [func first(where: (Output) -> Bool) -> Optional<Output>.Publisher](just/first(where:).md)
- [func last() -> Just<Output>](just/last.md)
- [func last(where: (Output) -> Bool) -> Optional<Output>.Publisher](just/last(where:).md)
- [func output(at: Int) -> Optional<Output>.Publisher](just/output(at:).md)
- [func output<R>(in: R) -> Optional<Output>.Publisher](just/output(in:).md)
### Handling errors
- [func retry(Int) -> Just<Output>](just/retry(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just-publisher-operators)*