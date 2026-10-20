# Publisher Operators

**Framework**: Combine  
**Role**: API Collection

Methods that create downstream publishers or subscribers to act on the elements they receive.

## Topics

### Mapping elements
- [func map<T>((Output) -> T) -> Just<T>](./just/map%28_%29.md)
- [func tryMap<T>((Output) throws -> T) -> Result<T, any Error>.Publisher](./just/trymap%28_%29.md)
- [func mapError<E>((Just<Output>.Failure) -> E) -> Result<Output, E>.Publisher](./just/maperror%28_%29.md)
- [func scan<T>(T, (T, Output) -> T) -> Result<T, Just<Output>.Failure>.Publisher](./just/scan%28_,_%29.md)
- [func tryScan<T>(T, (T, Output) throws -> T) -> Result<T, any Error>.Publisher](./just/tryscan%28_,_%29.md)
- [func setFailureType<E>(to: E.Type) -> Result<Output, E>.Publisher](./just/setfailuretype%28to%29.md)
### Filtering elements
- [func filter((Output) -> Bool) -> Optional<Output>.Publisher](./just/filter%28_%29.md)
- [func compactMap<T>((Output) -> T?) -> Optional<T>.Publisher](./just/compactmap%28_%29.md)
- [func removeDuplicates() -> Just<Output>](./just/removeduplicates%28%29.md)
- [func removeDuplicates(by: (Output, Output) -> Bool) -> Just<Output>](./just/removeduplicates%28by%29.md)
- [func tryRemoveDuplicates(by: (Output, Output) throws -> Bool) -> Result<Output, any Error>.Publisher](./just/tryremoveduplicates%28by%29.md)
- [func replaceEmpty(with: Output) -> Just<Output>](./just/replaceempty%28with%29.md)
- [func replaceError(with: Output) -> Just<Output>](./just/replaceerror%28with%29.md)
### Reducing elements
- [func collect() -> Just<[Output]>](./just/collect%28%29.md)
- [func ignoreOutput() -> Empty<Output, Just<Output>.Failure>](./just/ignoreoutput%28%29.md)
- [func reduce<T>(T, (T, Output) -> T) -> Result<T, Just<Output>.Failure>.Publisher](./just/reduce%28_,_%29.md)
- [func tryReduce<T>(T, (T, Output) throws -> T) -> Result<T, any Error>.Publisher](./just/tryreduce%28_,_%29.md)
### Applying mathematical operations on elements
- [func count() -> Just<Int>](./just/count%28%29.md)
- [func max() -> Just<Output>](./just/max%28%29.md)
- [func max(by: (Output, Output) -> Bool) -> Just<Output>](./just/max%28by%29.md)
- [func min() -> Just<Output>](./just/min%28%29.md)
- [func min(by: (Output, Output) -> Bool) -> Just<Output>](./just/min%28by%29.md)
### Applying matching criteria to elements
- [func contains(Output) -> Just<Bool>](./just/contains%28_%29.md)
- [func contains(where: (Output) -> Bool) -> Just<Bool>](./just/contains%28where%29.md)
- [func tryContains(where: (Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](./just/trycontains%28where%29.md)
- [func allSatisfy((Output) -> Bool) -> Just<Bool>](./just/allsatisfy%28_%29.md)
- [func tryAllSatisfy((Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](./just/tryallsatisfy%28_%29.md)
### Applying sequence operations to elements
- [func dropFirst(Int) -> Optional<Output>.Publisher](./just/dropfirst%28_%29.md)
- [func drop(while: (Output) -> Bool) -> Optional<Output>.Publisher](./just/drop%28while%29.md)
- [func append(Output...) -> Publishers.Sequence<[Output], Just<Output>.Failure>](./just/append%28_%29-7eyqj.md)
- [func append<S>(S) -> Publishers.Sequence<[Output], Just<Output>.Failure>](./just/append%28_%29-7sxlu.md)
- [func prepend<S>(S) -> Publishers.Sequence<[Output], Just<Output>.Failure>](./just/prepend%28_%29-39e57.md)
- [func prepend(Output...) -> Publishers.Sequence<[Output], Just<Output>.Failure>](./just/prepend%28_%29-7fg73.md)
- [func prefix(Int) -> Optional<Output>.Publisher](./just/prefix%28_%29.md)
- [func prefix(while: (Output) -> Bool) -> Optional<Output>.Publisher](./just/prefix%28while%29.md)
### Selecting specific elements
- [func first() -> Just<Output>](./just/first%28%29.md)
- [func first(where: (Output) -> Bool) -> Optional<Output>.Publisher](./just/first%28where%29.md)
- [func last() -> Just<Output>](./just/last%28%29.md)
- [func last(where: (Output) -> Bool) -> Optional<Output>.Publisher](./just/last%28where%29.md)
- [func output(at: Int) -> Optional<Output>.Publisher](./just/output%28at%29.md)
- [func output<R>(in: R) -> Optional<Output>.Publisher](./just/output%28in%29.md)
### Handling errors
- [func retry(Int) -> Just<Output>](./just/retry%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just-publisher-operators)*