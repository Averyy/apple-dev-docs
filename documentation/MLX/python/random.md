---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/random.html
---

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

Following [JAX’s PRNG design](https://jax.readthedocs.io/en/latest/jep/263-prng.html)
we use a splittable version of Threefry, which is a counter-based PRNG.

| [bernoulli](_autosummary/mlx.core.random.bernoulli.md#mlx.core.random.bernoulli)([p, shape, key, stream]) | Generate Bernoulli random values. |
| --- | --- |
| [categorical](_autosummary/mlx.core.random.categorical.md#mlx.core.random.categorical)(logits[, axis, shape, ...]) | Sample from a categorical distribution. |
| [gumbel](_autosummary/mlx.core.random.gumbel.md#mlx.core.random.gumbel)([shape, dtype, key, stream]) | Sample from the standard Gumbel distribution. |
| [key](_autosummary/mlx.core.random.key.md#mlx.core.random.key)(seed) | Get a PRNG key from a seed. |
| [normal](_autosummary/mlx.core.random.normal.md#mlx.core.random.normal)([shape, dtype, loc, scale, key, stream]) | Generate normally distributed random numbers. |
| [multivariate_normal](_autosummary/mlx.core.random.multivariate_normal.md#mlx.core.random.multivariate_normal)(mean, cov[, shape, ...]) | Generate jointly-normal random samples given a mean and covariance. |
| [randint](_autosummary/mlx.core.random.randint.md#mlx.core.random.randint)(low, high[, shape, dtype, key, stream]) | Generate random integers from the given interval. |
| [seed](_autosummary/mlx.core.random.seed.md#mlx.core.random.seed)(seed) | Seed the global PRNG. |
| [split](_autosummary/mlx.core.random.split.md#mlx.core.random.split)(key[, num, stream]) | Split a PRNG key into sub keys. |
| [truncated_normal](_autosummary/mlx.core.random.truncated_normal.md#mlx.core.random.truncated_normal)(lower, upper[, shape, ...]) | Generate values from a truncated normal distribution. |
| [uniform](_autosummary/mlx.core.random.uniform.md#mlx.core.random.uniform)([low, high, shape, dtype, key, stream]) | Generate uniformly distributed random numbers. |
| [laplace](_autosummary/mlx.core.random.laplace.md#mlx.core.random.laplace)([shape, dtype, loc, scale, key, stream]) | Sample numbers from a Laplace distribution. |
| [permutation](_autosummary/mlx.core.random.permutation.md#mlx.core.random.permutation)(x[, axis, key, stream]) | Generate a random permutation or permute the entries of an array. |
