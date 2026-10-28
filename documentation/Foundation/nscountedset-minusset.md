# minusSet:

**Framework**: Foundation  
**Role**: Article

Removes each object in another given set from the receiving set, if present.

## Overview

For each object in `otherSet` that is present in the set, this method decrements the associated count. If the count for an object is decremented to `0`, the object is removed from the set.

## See Also

### Related Documentation
- [class NSCountedSet](./nscountedset.md)
  A mutable, unordered collection of distinct objects that may appear more than once in the collection.
### Combining and Recombining Sets
- [unionSet:](./nscountedset-unionset.md)
  Adds each object in another given set to the receiving set, if not present.
- [intersectSet:](./nscountedset-intersectset.md)
  Removes from the receiving set each object that isn’t a member of another given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscountedset-minusset)*