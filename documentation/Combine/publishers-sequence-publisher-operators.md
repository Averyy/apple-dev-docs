# Publisher Operators

**Framework**: Combine  
**Role**: API Collection

Methods that create downstream publishers or subscribers to act on the elements they receive.

## Topics

### Mapping elements
- [func map<T>((Elements.Element) -> T) -> Publishers.Sequence<[T], Failure>](./publishers/sequence/map%28_%29.md)
- [func scan<T>(T, (T, Publishers.Sequence<Elements, Failure>.Output) -> T) -> Publishers.Sequence<[T], Failure>](./publishers/sequence/scan%28_,_%29.md)
- [func setFailureType<E>(to: E.Type) -> Publishers.Sequence<Elements, E>](./publishers/sequence/setfailuretype%28to%29.md)
- [func replaceNil<T>(with: T) -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure>](./publishers/sequence/replacenil%28with%29.md)
### Filtering elements
- [func filter((Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure>](./publishers/sequence/filter%28_%29.md)
- [func compactMap<T>((Publishers.Sequence<Elements, Failure>.Output) -> T?) -> Publishers.Sequence<[T], Failure>](./publishers/sequence/compactmap%28_%29.md)
- [func removeDuplicates() -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure>](./publishers/sequence/removeduplicates%28%29.md)
### Reducing elements
- [func collect() -> Result<[Publishers.Sequence<Elements, Failure>.Output], Failure>.Publisher](./publishers/sequence/collect%28%29.md)
- [func ignoreOutput() -> Empty<Publishers.Sequence<Elements, Failure>.Output, Failure>](./publishers/sequence/ignoreoutput%28%29.md)
- [func reduce<T>(T, (T, Publishers.Sequence<Elements, Failure>.Output) -> T) -> Result<T, Failure>.Publisher](./publishers/sequence/reduce%28_,_%29.md)
- [func tryReduce<T>(T, (T, Publishers.Sequence<Elements, Failure>.Output) throws -> T) -> Result<T, any Error>.Publisher](./publishers/sequence/tryreduce%28_,_%29.md)
### Applying mathematical operations on elements
- [func count() -> Just<Int>](./publishers/sequence/count%28%29-5rrw2.md)
- [func count() -> Result<Int, Failure>.Publisher](./publishers/sequence/count%28%29-5hb52.md)
- [func count() -> Result<Int, Failure>.Publisher](./publishers/sequence/count%28%29-b8ct.md)
- [func max() -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](./publishers/sequence/max%28%29.md)
- [func max(by: (Publishers.Sequence<Elements, Failure>.Output, Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](./publishers/sequence/max%28by%29.md)
- [func min() -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](./publishers/sequence/min%28%29.md)
- [func min(by: (Publishers.Sequence<Elements, Failure>.Output, Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](./publishers/sequence/min%28by%29.md)
### Applying matching criteria to elements
- [func contains(Elements.Element) -> Result<Bool, Failure>.Publisher](./publishers/sequence/contains%28_%29.md)
- [func contains(where: (Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Result<Bool, Failure>.Publisher](./publishers/sequence/contains%28where%29.md)
- [func tryContains(where: (Publishers.Sequence<Elements, Failure>.Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](./publishers/sequence/trycontains%28where%29.md)
- [func allSatisfy((Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Result<Bool, Failure>.Publisher](./publishers/sequence/allsatisfy%28_%29.md)
- [func tryAllSatisfy((Publishers.Sequence<Elements, Failure>.Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](./publishers/sequence/tryallsatisfy%28_%29.md)
### Applying sequence operations to elements
- [func dropFirst(Int) -> Publishers.Sequence<DropFirstSequence<Elements>, Failure>](./publishers/sequence/dropfirst%28_%29.md)
- [func drop(while: (Elements.Element) -> Bool) -> Publishers.Sequence<DropWhileSequence<Elements>, Failure>](./publishers/sequence/drop%28while%29.md)
- [func append<S>(S) -> Publishers.Sequence<Elements, Failure>](./publishers/sequence/append%28_%29-45rm8.md)
- [func append(Publishers.Sequence<Elements, Failure>) -> Publishers.Sequence<Elements, Failure>](./publishers/sequence/append%28_%29-3dj6k.md)
- [func append(Publishers.Sequence<Elements, Failure>.Output...) -> Publishers.Sequence<Elements, Failure>](./publishers/sequence/append%28_%29-2knh4.md)
- [func prepend<S>(S) -> Publishers.Sequence<Elements, Failure>](./publishers/sequence/prepend%28_%29-1r564.md)
- [func prepend(Publishers.Sequence<Elements, Failure>) -> Publishers.Sequence<Elements, Failure>](./publishers/sequence/prepend%28_%29-71f7p.md)
- [func prepend(Publishers.Sequence<Elements, Failure>.Output...) -> Publishers.Sequence<Elements, Failure>](./publishers/sequence/prepend%28_%29-2ros1.md)
- [func prefix(Int) -> Publishers.Sequence<PrefixSequence<Elements>, Failure>](./publishers/sequence/prefix%28_%29.md)
- [func prefix(while: (Elements.Element) -> Bool) -> Publishers.Sequence<[Elements.Element], Failure>](./publishers/sequence/prefix%28while%29.md)
### Selecting specific elements
- [func first() -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](./publishers/sequence/first%28%29.md)
- [func first(where: (Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](./publishers/sequence/first%28where%29.md)
- [func last() -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](./publishers/sequence/last%28%29.md)
- [func last(where: (Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](./publishers/sequence/last%28where%29.md)
- [func output(at: Elements.Index) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](./publishers/sequence/output%28at%29-3r7zo.md)
- [func output(at: Elements.Index) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](./publishers/sequence/output%28at%29-9kto7.md)
- [func output(in: Range<Elements.Index>) -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure>](./publishers/sequence/output%28in%29-6g2zc.md)
- [func output(in: Range<Elements.Index>) -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure>](./publishers/sequence/output%28in%29-8l6yw.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers-sequence-publisher-operators)*