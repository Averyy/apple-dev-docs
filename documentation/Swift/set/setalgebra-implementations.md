# SetAlgebra Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Initializers
- [init()](./init%28%29.md)
  Creates an empty set.
- [init<Source>(Source)](./init%28_%29.md)
  Creates a new set from a finite sequence of items.
- [init<S>(S)](./init%28_%29-9cgks.md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](./init%28arrayliteral%29-85a3x.md)
  Creates a set containing the elements of the given array literal.
### Instance Methods
- [func contains(Element) -> Bool](./contains%28_%29.md)
  Returns a Boolean value that indicates whether the given element exists in the set.
- [func formIntersection<S>(S)](./formintersection%28_%29.md)
  Removes the elements of the set that aren’t also in the given sequence.
- [func formSymmetricDifference(Set<Element>)](./formsymmetricdifference%28_%29-22p0m.md)
  Removes the elements of the set that are also in the given sequence and adds the members of the sequence that are not already in the set.
- [func formUnion<S>(S)](./formunion%28_%29.md)
  Inserts the elements of the given sequence into the set.
- [func insert(Element) -> (inserted: Bool, memberAfterInsert: Element)](./insert%28_%29-nads.md)
  Inserts the given element in the set if it is not already present.
- [func intersection(Set<Element>) -> Set<Element>](./intersection%28_%29-1zh8f.md)
  Returns a new set with the elements that are common to both this set and the given sequence.
- [func isDisjoint(with: Set<Element>) -> Bool](./isdisjoint%28with%29-8ngmk.md)
  Returns a Boolean value that indicates whether this set has no members in common with the given set.
- [func isSubset(of: Set<Element>) -> Bool](./issubset%28of%29-1d7pp.md)
  Returns a Boolean value that indicates whether this set is a subset of the given set.
- [func isSuperset(of: Set<Element>) -> Bool](./issuperset%28of%29-9iz62.md)
  Returns a Boolean value that indicates whether this set is a superset of the given set.
- [func remove(Element) -> Element?](./remove%28_%29-8p2tv.md)
  Removes the specified element from the set.
- [func subtract(Self)](./subtract%28_%29-7uaak.md)
  Removes the elements of the given set from this set.
- [func subtract(Set<Element>)](./subtract%28_%29-8gc48.md)
  Removes the elements of the given set from this set.
- [func subtracting(Set<Element>) -> Set<Element>](./subtracting%28_%29-3n4lc.md)
  Returns a new set containing the elements of this set that do not occur in the given set.
- [func symmetricDifference<S>(S) -> Set<Element>](./symmetricdifference%28_%29.md)
  Returns a new set with the elements that are either in this set or in the given sequence, but not in both.
- [func union<S>(S) -> Set<Element>](./union%28_%29.md)
  Returns a new set with the elements of both this set and the given sequence.
- [func update(with: Element) -> Element?](./update%28with%29-2n6tk.md)
  Inserts the given element into the set unconditionally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/setalgebra-implementations)*