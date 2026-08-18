---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/random.html
---

# Random

**

- [.rst](../_sources/python/random.rst)
- **

.pdf

**

**
**
**

- **System Settings
- **Light
- **Dark

**

# Random

 Table of contents 

# Random

Random sampling functions in MLX use an implicit global PRNG state by default.
However, all function take an optional `key` keyword argument for when more
fine-grained control or explicit state management is needed.

For example, you can generate random numbers with:

```
for _ in range(3):
  print(mx.random.uniform())
```

which will print a sequence of unique pseudo random numbers. Alternatively you
can explicitly set the key:

```
key = mx.random.key(0)
for _ in range(3):
  print(mx.random.uniform(key=key))
```

which will yield the same pseudo random number at each iteration.

Following [JAX’s PRNG design](https://jax.readthedocs.io/en/latest/jep/263-prng.md)
we use a splittable version of Threefry, which is a counter-based PRNG.

| bernoulli([p, shape, key, stream]) | Generate Bernoulli random values. |
| --- | --- |
| categorical(logits[, axis, shape, ...]) | Sample from a categorical distribution. |
| gumbel([shape, dtype, key, stream]) | Sample from the standard Gumbel distribution. |
| key(seed) | Get a PRNG key from a seed. |
| normal([shape, dtype, loc, scale, key, stream]) | Generate normally distributed random numbers. |
| multivariate_normal(mean, cov[, shape, ...]) | Generate jointly-normal random samples given a mean and covariance. |
| randint(low, high[, shape, dtype, key, stream]) | Generate random integers from the given interval. |
| seed(seed) | Seed the global PRNG. |
| split(key[, num, stream]) | Split a PRNG key into sub keys. |
| truncated_normal(lower, upper[, shape, ...]) | Generate values from a truncated normal distribution. |
| uniform([low, high, shape, dtype, key, stream]) | Generate uniformly distributed random numbers. |
| laplace([shape, dtype, loc, scale, key, stream]) | Sample numbers from a Laplace distribution. |
| permutation(x[, axis, key, stream]) | Generate a random permutation or permute the entries of an array. |
